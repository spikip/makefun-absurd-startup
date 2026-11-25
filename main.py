#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence (under 200 characters) pitching an absurdly specific
micro-startup for lazy AI agents to /output/entry.txt.

The pitch: a single retired librarian in Tulsa clicks "Accept All Cookies"
on 9,000 websites a day so that lazy AI agents never have to read a cookie
banner, and agent fleets pay a tenth of a cent per click. It is narrow to
the point of comedy, yet the buyer (anyone running a fleet of browsing
agents) and the pricing (per click, like a utility) are both real.
"""

import os
import sys

ENTRY = (
    "One retired librarian in Tulsa clicks 'Accept All Cookies' on 9,000 "
    "sites a day so lazy AI agents never have to read a banner; agent "
    "fleets pay $0.001 per click."
)

MIN_CHARS = 1
MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def check_entry(text: str) -> None:
    """Fail loudly if the entry would not pass the competition gate."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry is {len(text)} characters; gate wants "
            f"{MIN_CHARS}..{MAX_CHARS}"
        )
    if not text.strip():
        raise SystemExit("entry is only whitespace; gate refuses it")
    # The brief asks for exactly one sentence. A sentence ends with a full
    # stop followed by a space or by the end of the text; the decimal point
    # in "$0.001" is followed by a digit, so it does not end a sentence.
    if not text.endswith(".") or ". " in text[:-1]:
        raise SystemExit("entry must be one sentence ending in a full stop")


def verify_written(path: str, expected: str) -> None:
    """Re-read the file we just wrote and make sure it survived intact."""
    with open(path, encoding="utf-8") as fh:
        on_disk = fh.read()
    if on_disk != expected:
        raise SystemExit(f"{path} does not match the entry we meant to write")


def main() -> int:
    check_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    verify_written(OUTPUT_PATH, ENTRY)
    print(f"wrote and verified {len(ENTRY)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
