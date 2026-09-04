# mini_llama

A small, dependency-light PyTorch implementation of a Llama-style decoder-only
transformer language model, built from scratch for learning and
experimentation. It is not a copy of Meta's Llama weights or code — it
reimplements the architectural ideas that define the Llama model family:

- **RMSNorm** instead of LayerNorm (`model.py::RMSNorm`)
- **Rotary position embeddings (RoPE)** instead of learned position
  embeddings (`model.py::apply_rope`)
- **SwiGLU** gated feed-forward blocks (`model.py::SwiGLU`)
- **Grouped-query attention (GQA)**, which also covers plain multi-head and
  multi-query attention as special cases (`model.py::Attention`)
- **Pre-normalization** residual blocks and a **KV cache** for fast
  autoregressive generation (`model.py::TransformerBlock`,
  `model.py::Transformer.generate`)
- Weight tying between the input embedding and output projection

## Layout

```
mini_llama/
  model.py       Transformer architecture
  tokenizer.py   Minimal byte-level tokenizer (vocab size 256, no training needed)
  train.py       Training loop (next-token prediction on a text file)
  generate.py    Load a checkpoint and sample text from a prompt
  data/tiny_corpus.txt   Small sample corpus for smoke-testing the pipeline
```

## Quickstart

```bash
pip install -r requirements.txt

# Train a small model on the sample corpus (CPU-friendly settings)
python3 train.py --data data/tiny_corpus.txt --dim 128 --n_layers 4 \
    --n_heads 4 --n_kv_heads 2 --seq_len 64 --batch_size 16 --steps 300

# Generate text from the trained checkpoint
python3 generate.py --checkpoint checkpoint.pt --prompt "Saturn is" \
    --max_new_tokens 200
```

To train on your own data, point `--data` at any UTF-8 text file. Model size
is controlled by `--dim`, `--n_layers`, `--n_heads`, and `--n_kv_heads`
(set `--n_kv_heads` lower than `--n_heads` to use grouped-query attention and
shrink the KV cache).

## Scaling up

This is a toy-scale reference implementation (a few million parameters,
byte-level tokenization, single-GPU/CPU training loop) meant to make the
Llama architecture easy to read end to end. To approach real Llama-sized
models you would additionally need: a proper subword tokenizer (e.g. BPE),
a much larger and cleaned training corpus, distributed/mixed-precision
training, and many more layers/parameters trained for many more steps.
