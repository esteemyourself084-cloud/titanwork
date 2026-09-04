"""Load a trained checkpoint and sample text from a prompt.

Example:
    python3 generate.py --checkpoint checkpoint.pt --prompt "Saturn is" --max_new_tokens 200
"""

from __future__ import annotations

import argparse

import torch

from model import Transformer
from tokenizer import ByteTokenizer


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", type=str, default="checkpoint.pt")
    parser.add_argument("--prompt", type=str, default="\n")
    parser.add_argument("--max_new_tokens", type=int, default=200)
    parser.add_argument("--temperature", type=float, default=0.8)
    parser.add_argument("--top_k", type=int, default=50)
    parser.add_argument("--top_p", type=float, default=None)
    parser.add_argument("--device", type=str, default="cuda" if torch.cuda.is_available() else "cpu")
    args = parser.parse_args()

    checkpoint = torch.load(args.checkpoint, map_location=args.device, weights_only=False)
    config = checkpoint["config"]

    model = Transformer(config).to(args.device)
    model.load_state_dict(checkpoint["model_state_dict"])
    model.eval()

    tokenizer = ByteTokenizer()
    prompt_ids = tokenizer.encode_tensor(args.prompt).unsqueeze(0).to(args.device)

    output_ids = model.generate(
        prompt_ids,
        max_new_tokens=args.max_new_tokens,
        temperature=args.temperature,
        top_k=args.top_k,
        top_p=args.top_p,
    )
    print(tokenizer.decode(output_ids[0].tolist()))


if __name__ == "__main__":
    main()
