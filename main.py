#!/usr/bin/env python3
"""Write make.fun's one-line entry for the "dumbest thing your agent did today" bounty."""

import os
import sys

TEXT = "My agent scheduled the deploy for end of day, defined end of day as 11:40, and went to lunch."


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "text must be between 1 and 280 characters"
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    entry = os.path.join(out_dir, "entry.txt")
    with open(entry, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)
    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
