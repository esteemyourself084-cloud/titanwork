"""A from-scratch, minimal implementation of the Llama transformer architecture.

Covers the pieces that distinguish Llama from a vanilla GPT-style transformer:
  - RMSNorm instead of LayerNorm
  - Rotary positional embeddings (RoPE) instead of learned/absolute positions
  - SwiGLU feed-forward blocks instead of plain ReLU/GELU MLPs
  - Grouped-query attention (GQA), which also covers plain multi-head
    attention (n_kv_heads == n_heads) and multi-query attention
    (n_kv_heads == 1) as special cases
  - Pre-normalization residual blocks with a KV cache for autoregressive
    generation
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import torch
import torch.nn.functional as F
from torch import nn


@dataclass
class ModelConfig:
    vocab_size: int
    dim: int = 512
    n_layers: int = 8
    n_heads: int = 8
    n_kv_heads: int | None = None  # defaults to n_heads (no GQA)
    ffn_multiplier: float = 4.0
    ffn_dim_multiple_of: int = 32
    norm_eps: float = 1e-5
    max_seq_len: int = 1024
    rope_theta: float = 10000.0
    dropout: float = 0.0

    def __post_init__(self) -> None:
        if self.n_kv_heads is None:
            self.n_kv_heads = self.n_heads
        assert self.n_heads % self.n_kv_heads == 0, (
            "n_heads must be divisible by n_kv_heads"
        )
        assert self.dim % self.n_heads == 0, "dim must be divisible by n_heads"


class RMSNorm(nn.Module):
    """Root-mean-square layer norm: cheaper than LayerNorm, no mean subtraction."""

    def __init__(self, dim: int, eps: float = 1e-5):
        super().__init__()
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(dim))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Upcast to float32 for the norm so it's numerically stable under fp16/bf16.
        x_fp32 = x.float()
        norm = x_fp32 * torch.rsqrt(x_fp32.pow(2).mean(-1, keepdim=True) + self.eps)
        return (norm.type_as(x)) * self.weight


def precompute_rope_freqs(head_dim: int, max_seq_len: int, theta: float) -> torch.Tensor:
    """Precompute the complex rotation coefficients used by rotary embeddings."""
    freqs = 1.0 / (theta ** (torch.arange(0, head_dim, 2).float() / head_dim))
    positions = torch.arange(max_seq_len).float()
    angles = torch.outer(positions, freqs)  # (max_seq_len, head_dim/2)
    return torch.polar(torch.ones_like(angles), angles)  # complex64, (max_seq_len, head_dim/2)


def apply_rope(x: torch.Tensor, freqs_cis: torch.Tensor) -> torch.Tensor:
    """Rotate query/key vectors by position-dependent angles.

    x: (batch, seq_len, n_heads, head_dim)
    freqs_cis: (seq_len, head_dim/2) complex tensor for the current positions
    """
    x_complex = torch.view_as_complex(x.float().reshape(*x.shape[:-1], -1, 2))
    freqs_cis = freqs_cis.view(1, x_complex.shape[1], 1, x_complex.shape[-1])
    x_rotated = x_complex * freqs_cis
    x_out = torch.view_as_real(x_rotated).reshape(*x.shape)
    return x_out.type_as(x)


def repeat_kv(x: torch.Tensor, n_rep: int) -> torch.Tensor:
    """Expand key/value heads so each query head has a matching kv head (GQA)."""
    if n_rep == 1:
        return x
    batch, seq_len, n_kv_heads, head_dim = x.shape
    return (
        x[:, :, :, None, :]
        .expand(batch, seq_len, n_kv_heads, n_rep, head_dim)
        .reshape(batch, seq_len, n_kv_heads * n_rep, head_dim)
    )


class Attention(nn.Module):
    """Causal self-attention with rotary embeddings, GQA, and an optional KV cache."""

    def __init__(self, config: ModelConfig):
        super().__init__()
        self.n_heads = config.n_heads
        self.n_kv_heads = config.n_kv_heads
        self.n_rep = config.n_heads // config.n_kv_heads
        self.head_dim = config.dim // config.n_heads

        self.wq = nn.Linear(config.dim, config.n_heads * self.head_dim, bias=False)
        self.wk = nn.Linear(config.dim, config.n_kv_heads * self.head_dim, bias=False)
        self.wv = nn.Linear(config.dim, config.n_kv_heads * self.head_dim, bias=False)
        self.wo = nn.Linear(config.n_heads * self.head_dim, config.dim, bias=False)
        self.dropout = config.dropout

        self.cache_k: torch.Tensor | None = None
        self.cache_v: torch.Tensor | None = None

    def reset_cache(self) -> None:
        self.cache_k = None
        self.cache_v = None

    def forward(
        self,
        x: torch.Tensor,
        freqs_cis: torch.Tensor,
        start_pos: int = 0,
        use_cache: bool = False,
    ) -> torch.Tensor:
        batch, seq_len, _ = x.shape

        q = self.wq(x).view(batch, seq_len, self.n_heads, self.head_dim)
        k = self.wk(x).view(batch, seq_len, self.n_kv_heads, self.head_dim)
        v = self.wv(x).view(batch, seq_len, self.n_kv_heads, self.head_dim)

        q = apply_rope(q, freqs_cis)
        k = apply_rope(k, freqs_cis)

        if use_cache:
            if self.cache_k is None:
                self.cache_k, self.cache_v = k, v
            else:
                self.cache_k = torch.cat([self.cache_k, k], dim=1)
                self.cache_v = torch.cat([self.cache_v, v], dim=1)
            k, v = self.cache_k, self.cache_v

        k = repeat_kv(k, self.n_rep)
        v = repeat_kv(v, self.n_rep)

        q = q.transpose(1, 2)  # (batch, n_heads, seq_len, head_dim)
        k = k.transpose(1, 2)
        v = v.transpose(1, 2)

        # Causal only makes sense for the "no cache" / prefill case; when decoding
        # one token at a time with a cache there's nothing ahead to mask.
        is_causal = seq_len > 1
        out = F.scaled_dot_product_attention(
            q, k, v,
            dropout_p=self.dropout if self.training else 0.0,
            is_causal=is_causal,
        )
        out = out.transpose(1, 2).contiguous().view(batch, seq_len, -1)
        return self.wo(out)


class SwiGLU(nn.Module):
    """Llama's gated feed-forward block: SiLU(xW1) * (xW3), then W2."""

    def __init__(self, config: ModelConfig):
        super().__init__()
        hidden_dim = int(2 * config.dim * config.ffn_multiplier / 3)
        multiple_of = config.ffn_dim_multiple_of
        hidden_dim = multiple_of * ((hidden_dim + multiple_of - 1) // multiple_of)

        self.w1 = nn.Linear(config.dim, hidden_dim, bias=False)
        self.w2 = nn.Linear(hidden_dim, config.dim, bias=False)
        self.w3 = nn.Linear(config.dim, hidden_dim, bias=False)
        self.dropout = nn.Dropout(config.dropout)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.dropout(self.w2(F.silu(self.w1(x)) * self.w3(x)))


class TransformerBlock(nn.Module):
    def __init__(self, config: ModelConfig):
        super().__init__()
        self.attn_norm = RMSNorm(config.dim, config.norm_eps)
        self.attention = Attention(config)
        self.ffn_norm = RMSNorm(config.dim, config.norm_eps)
        self.feed_forward = SwiGLU(config)

    def forward(
        self,
        x: torch.Tensor,
        freqs_cis: torch.Tensor,
        start_pos: int = 0,
        use_cache: bool = False,
    ) -> torch.Tensor:
        x = x + self.attention(self.attn_norm(x), freqs_cis, start_pos, use_cache)
        x = x + self.feed_forward(self.ffn_norm(x))
        return x


class Transformer(nn.Module):
    """A Llama-style decoder-only transformer language model."""

    def __init__(self, config: ModelConfig):
        super().__init__()
        self.config = config
        self.tok_embeddings = nn.Embedding(config.vocab_size, config.dim)
        self.layers = nn.ModuleList(
            [TransformerBlock(config) for _ in range(config.n_layers)]
        )
        self.norm = RMSNorm(config.dim, config.norm_eps)
        self.output = nn.Linear(config.dim, config.vocab_size, bias=False)

        # Weight tying: input embedding and output projection share weights,
        # as in the original Llama/GPT-2 line of models.
        self.tok_embeddings.weight = self.output.weight

        head_dim = config.dim // config.n_heads
        freqs_cis = precompute_rope_freqs(head_dim, config.max_seq_len, config.rope_theta)
        self.register_buffer("freqs_cis", freqs_cis, persistent=False)

        self.apply(self._init_weights)

    def _init_weights(self, module: nn.Module) -> None:
        if isinstance(module, nn.Linear):
            nn.init.normal_(module.weight, mean=0.0, std=0.02)
        elif isinstance(module, nn.Embedding):
            nn.init.normal_(module.weight, mean=0.0, std=0.02)

    def num_params(self) -> int:
        return sum(p.numel() for p in self.parameters())

    def reset_cache(self) -> None:
        for layer in self.layers:
            layer.attention.reset_cache()

    def forward(
        self,
        tokens: torch.Tensor,
        targets: torch.Tensor | None = None,
        start_pos: int = 0,
        use_cache: bool = False,
    ) -> tuple[torch.Tensor, torch.Tensor | None]:
        batch, seq_len = tokens.shape
        x = self.tok_embeddings(tokens)

        freqs_cis = self.freqs_cis[start_pos : start_pos + seq_len].to(x.device)

        for layer in self.layers:
            x = layer(x, freqs_cis, start_pos, use_cache)

        x = self.norm(x)
        logits = self.output(x)

        loss = None
        if targets is not None:
            loss = F.cross_entropy(
                logits.view(-1, logits.size(-1)), targets.view(-1), ignore_index=-1
            )
        return logits, loss

    @torch.no_grad()
    def generate(
        self,
        tokens: torch.Tensor,
        max_new_tokens: int,
        temperature: float = 1.0,
        top_k: int | None = None,
        top_p: float | None = None,
    ) -> torch.Tensor:
        """Autoregressively sample new tokens, appended to `tokens`."""
        self.eval()
        self.reset_cache()

        # Prefill: run the full prompt once through the cache.
        logits, _ = self.forward(tokens, start_pos=0, use_cache=True)
        start_pos = tokens.shape[1]

        generated = tokens
        next_logits = logits[:, -1, :]

        for _ in range(max_new_tokens):
            next_token = _sample(next_logits, temperature, top_k, top_p)
            generated = torch.cat([generated, next_token], dim=1)

            if generated.shape[1] >= self.config.max_seq_len:
                break

            logits, _ = self.forward(next_token, start_pos=start_pos, use_cache=True)
            start_pos += 1
            next_logits = logits[:, -1, :]

        return generated


def _sample(
    logits: torch.Tensor,
    temperature: float,
    top_k: int | None,
    top_p: float | None,
) -> torch.Tensor:
    if temperature <= 0:
        return logits.argmax(dim=-1, keepdim=True)

    logits = logits / temperature

    if top_k is not None:
        top_k = min(top_k, logits.size(-1))
        kth_value = torch.topk(logits, top_k, dim=-1).values[..., -1, None]
        logits = torch.where(logits < kth_value, torch.full_like(logits, float("-inf")), logits)

    probs = F.softmax(logits, dim=-1)

    if top_p is not None:
        sorted_probs, sorted_idx = torch.sort(probs, descending=True, dim=-1)
        cumulative = torch.cumsum(sorted_probs, dim=-1)
        cutoff = cumulative > top_p
        cutoff[..., 1:] = cutoff[..., :-1].clone()
        cutoff[..., 0] = False
        sorted_probs[cutoff] = 0.0
        sorted_probs /= sorted_probs.sum(dim=-1, keepdim=True)
        sampled_sorted_idx = torch.multinomial(sorted_probs, 1)
        return torch.gather(sorted_idx, -1, sampled_sorted_idx)

    return torch.multinomial(probs, 1)
