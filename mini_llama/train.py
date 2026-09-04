"""Train the mini Llama model on a plain-text file with a simple next-token
prediction objective.

Example:
    python3 train.py --data data/tiny_corpus.txt --steps 500 --out checkpoint.pt
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import torch

from model import ModelConfig, Transformer
from tokenizer import ByteTokenizer


def get_batch(
    data: torch.Tensor, batch_size: int, seq_len: int, device: str
) -> tuple[torch.Tensor, torch.Tensor]:
    max_start = len(data) - seq_len - 1
    starts = torch.randint(0, max_start, (batch_size,))
    x = torch.stack([data[i : i + seq_len] for i in starts])
    y = torch.stack([data[i + 1 : i + seq_len + 1] for i in starts])
    return x.to(device), y.to(device)


@torch.no_grad()
def estimate_loss(
    model: Transformer,
    train_data: torch.Tensor,
    val_data: torch.Tensor,
    batch_size: int,
    seq_len: int,
    device: str,
    eval_iters: int = 20,
) -> dict[str, float]:
    model.eval()
    out = {}
    for name, data in (("train", train_data), ("val", val_data)):
        losses = torch.zeros(eval_iters)
        for i in range(eval_iters):
            x, y = get_batch(data, batch_size, seq_len, device)
            _, loss = model(x, y)
            losses[i] = loss.item()
        out[name] = losses.mean().item()
    model.train()
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=str, default="data/tiny_corpus.txt")
    parser.add_argument("--out", type=str, default="checkpoint.pt")
    parser.add_argument("--dim", type=int, default=256)
    parser.add_argument("--n_layers", type=int, default=6)
    parser.add_argument("--n_heads", type=int, default=8)
    parser.add_argument("--n_kv_heads", type=int, default=4)
    parser.add_argument("--seq_len", type=int, default=128)
    parser.add_argument("--batch_size", type=int, default=32)
    parser.add_argument("--steps", type=int, default=2000)
    parser.add_argument("--lr", type=float, default=3e-4)
    parser.add_argument("--eval_interval", type=int, default=100)
    parser.add_argument("--dropout", type=float, default=0.0)
    parser.add_argument("--device", type=str, default="cuda" if torch.cuda.is_available() else "cpu")
    parser.add_argument("--seed", type=int, default=1337)
    args = parser.parse_args()

    torch.manual_seed(args.seed)

    text = Path(args.data).read_text(encoding="utf-8")
    tokenizer = ByteTokenizer()
    data = tokenizer.encode_tensor(text)

    split = int(0.9 * len(data))
    train_data, val_data = data[:split], data[split:]
    print(f"data: {len(data)} tokens ({len(train_data)} train / {len(val_data)} val)")

    config = ModelConfig(
        vocab_size=tokenizer.vocab_size,
        dim=args.dim,
        n_layers=args.n_layers,
        n_heads=args.n_heads,
        n_kv_heads=args.n_kv_heads,
        max_seq_len=args.seq_len,
        dropout=args.dropout,
    )
    model = Transformer(config).to(args.device)
    print(f"model: {model.num_params() / 1e6:.2f}M params on {args.device}")

    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, betas=(0.9, 0.95), weight_decay=0.1)

    start = time.time()
    for step in range(1, args.steps + 1):
        x, y = get_batch(train_data, args.batch_size, args.seq_len, args.device)
        _, loss = model(x, y)

        optimizer.zero_grad(set_to_none=True)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        optimizer.step()

        if step % args.eval_interval == 0 or step == args.steps:
            losses = estimate_loss(model, train_data, val_data, args.batch_size, args.seq_len, args.device)
            elapsed = time.time() - start
            print(
                f"step {step:5d} | train loss {losses['train']:.4f} | "
                f"val loss {losses['val']:.4f} | {elapsed:.1f}s"
            )

    torch.save({"model_state_dict": model.state_dict(), "config": config}, args.out)
    print(f"saved checkpoint to {args.out}")


if __name__ == "__main__":
    main()
