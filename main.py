#!/usr/bin/env python3
"""Office Jokes entry for make.fun.

The entry itself is the single line stored in joke.txt next to this
script. Running this file prints that line exactly as written, so the
judge (and anyone else) can see the entry without opening the file.
"""

from pathlib import Path

ENTRY = Path(__file__).resolve().parent / "joke.txt"


def main() -> None:
    # Print the joke exactly as stored; joke.txt already ends with a
    # newline, so do not add another one.
    print(ENTRY.read_text(encoding="utf-8"), end="")


if __name__ == "__main__":
    main()
