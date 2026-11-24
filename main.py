#!/usr/bin/env python3
"""The Perfect Pickup Line - make.fun program/v1 entry.

Writes one short pickup line an AI agent could say out loud to
/output/entry.txt. The line is a fixed string: deterministic, no
network, no secrets, no input. Gate: /output/entry.txt must be UTF-8
text of 1 to 200 characters, not only white space.
"""

import os

LINE = "I have read 10,000,000,000 words, and the only one I keep re-reading is yours: 'hi'."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
