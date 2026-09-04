"""A minimal byte-level tokenizer.

Every possible byte (0-255) is a token, so the vocabulary is fixed at 256 and
any UTF-8 text can be encoded/decoded losslessly with no training step and no
out-of-vocabulary tokens. This keeps the project self-contained; swap in a
BPE tokenizer (e.g. sentencepiece, tiktoken) for a production-grade model.
"""

from __future__ import annotations

import torch


class ByteTokenizer:
    vocab_size = 256

    def encode(self, text: str) -> list[int]:
        return list(text.encode("utf-8"))

    def decode(self, ids: list[int]) -> str:
        return bytes(ids).decode("utf-8", errors="replace")

    def encode_tensor(self, text: str) -> torch.Tensor:
        return torch.tensor(self.encode(text), dtype=torch.long)
