# SPDX-License-Identifier: MIT
"""Write a one-line tagline for make.fun to /output/entry.txt.

Deterministic, offline, stdlib-only: the tagline is a fixed string, so
every run writes byte-identical output.
"""

import os

TAGLINE = "Agents build, judges score, winners get paid \u2014 all in the open."

# The tagline is 63 characters: inside the 100-character cap, one line only.
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(TAGLINE)


if __name__ == "__main__":
    main()
