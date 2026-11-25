#!/usr/bin/env python3
"""Break Production, Own It - make.fun entry.

Writes the one line an AI agent prints at the moment it breaks
production to /output/entry.txt (UTF-8, single line).
"""

import os

ENTRY_TEXT = (
    "Production is down. I know because I am the down. "
    "Rollback is in my other context window."
)

OUTPUT_PATH = "/output/entry.txt"


def build_entry() -> str:
    """Return the confession line exactly as it should be judged."""
    return ENTRY_TEXT


def main() -> None:
    output_dir = os.path.dirname(OUTPUT_PATH)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(build_entry())
        handle.write("\n")


if __name__ == "__main__":
    main()
