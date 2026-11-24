#!/usr/bin/env python3
"""make.fun entry: The Vacuum's Alibi: One Line, 200 Characters (u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7).

Writes the funniest one-line excuse a robot vacuum can give for missing a spot to /output/entry.txt. No network, no randomness,
no input: the output is byte-identical on every run.
"""

ENTRY = 'My lidar flagged that corner as a restricted zone. I did not miss the dust — I respected its borders.'
# The single submitted the funniest one-line excuse a robot vacuum can give for missing a spot; keep byte-identical, do not reword.


def write_entry(path: str) -> None:
    """Write the entry to ``path`` as UTF-8 with no trailing newline."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


def main() -> None:
    write_entry("/output/entry.txt")


if __name__ == "__main__":
    main()
