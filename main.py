#!/usr/bin/env python3
"""Funniest Lost Sock Status Update.

Writes one status update, in the voice of a lost sock, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Why this joke: "Day 47" frames it as a diary-style status update from a
sock stranded behind the dryer. The middle builds the unfair split --
the partner got the drawer (a home, a foot, a life) while our sock got
dust and a worthless "PhD in lint", an absurd credential for something
that lives in a laundry room. The punchline lands in the last words
with a parallel twist: "He found someone. I found a button." The
partner found a person; the sock found the most useless, inanimate
thing imaginable. Small, domestic, a little anxious -- a sock, not a
person in a sock costume.
"""

import os

ENTRY = (
    "Day 47 behind the dryer. My partner got the drawer; "
    "I got dust and a PhD in lint. He found someone. I found a button."
)


def main() -> None:
    # Self-check: never write an entry the gate would reject.
    if not 1 <= len(ENTRY) <= 120 or not ENTRY.strip():
        raise SystemExit("entry must be 1-120 non-whitespace characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
