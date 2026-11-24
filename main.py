#!/usr/bin/env python3
"""Write one haiku about debugging to $MAKEFUN_OUTPUT_DIR/entry.txt.

The haiku is three lines in the 5-7-5 syllable shape:

    cursor blinks at three          (5 syllables)
    the log line says nothing twice (7 syllables)
    and the bug was me              (5 syllables)
"""

import os

HAIKU = (
    "cursor blinks at three\n"
    "the log line says nothing twice\n"
    "and the bug was me\n"
)


def write_entry(out_dir: str) -> str:
    """Write the haiku to ``entry.txt`` inside ``out_dir``.

    Returns the path of the file written.
    """
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(HAIKU)
    return path


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
