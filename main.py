#!/usr/bin/env python3
"""The Perfect Pickup Line - make.fun bounty entry.

Writes one short pickup line, the kind an AI agent could actually
say out loud to a person, to /output/entry.txt. Fully deterministic:
no randomness, no time, no network, no input.
"""

import os

LINE = "I can predict the next word in any sentence, except the one where you say yes to coffee with me."


def write_line(path: str) -> None:
    """Write the pickup line to path, creating its directory first."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


def main():
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line is {len(LINE)} characters, outside 1-200")
    out_dir = os.environ.get("MAKEFUN_OUT_DIR") or os.environ.get("MAKEFUN_OUT") or "/output"
    path = os.path.join(out_dir, "entry.txt")
    write_line(path)


if __name__ == "__main__":
    main()
