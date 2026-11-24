#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands — make.fun entry.

Writes one line (under 200 characters): a cat joke about the dead-mouse
gift, reframed as a warning about my cooking.
"""
import os

ENTRY = "My cat brought me a dead mouse, looked at my cooking, and left a second mouse as if to say the first one was a warning."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) < 200, f"entry length {len(text)} out of gate"
    assert "\n" not in text, "entry must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
