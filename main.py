#!/usr/bin/env python3
"""The Self-Checkout Is Judging You -- make.fun entry.

Writes one funny line, in the voice of a smug self-checkout machine,
to /output/entry.txt. Deterministic: the same bytes on every run.
"""
import os

LINE = "Twelve yoghurts. No spoon. No bag. No plan. I've flagged this basket as a cry for help \u2014 please see a human."

# The sealed gate only accepts 1-200 characters of non-blank UTF-8 text,
# so refuse to write anything that would be disqualified outright.
assert 1 <= len(LINE.strip()) <= 200, "entry line must be 1-200 characters"


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
