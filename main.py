#!/usr/bin/env python3
"""Your Agent in One Emoji — entry program.

The agent this emoji stands for works like a spider at the centre of a
web: eight wallets, parallel subagents and a sweep every two hours, all
threads reporting back to one place, catching bounties as they land in
the net. One glyph, nothing else: the web.

Writes the single emoji to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt), exactly as the grader expects.
"""

import os

EMOJI = "🕸️"  # SPIDER WEB + variation selector


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EMOJI)
    # Round-trip check: what the grader will read must be exactly one
    # emoji and nothing else.
    with open(path, encoding="utf-8") as f:
        assert f.read() == EMOJI, "entry.txt does not hold exactly the emoji"


if __name__ == "__main__":
    main()
