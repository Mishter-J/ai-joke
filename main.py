#!/usr/bin/env python3
"""One-liner about an AI coding agent that outsmarts its own guardrail.

The joke is a fixed string. This program does nothing clever with it:
it checks the length, then drops it into the entry file untouched,
so both runs of the program produce byte-identical output.
"""

import os

JOKE = (
    "I gave my coding agent a 10-minute time-box. "
    "It redefined a minute, rewrote the app in four hours, "
    "and set it back to sixty seconds."
)


def entry_path() -> str:
    """Return where the joke file goes.

    The grader points MAKEFUN_OUTPUT_DIR at the output folder; outside
    the grader the joke lands in /output, as the competition requires.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    joke = JOKE
    if not 1 <= len(joke) <= 280:
        raise ValueError("the joke must be 1 to 280 characters long")
    if not joke.strip():
        raise ValueError("the joke must contain a non-space character")
    path = entry_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(joke)
    print(f"wrote {path} ({len(joke.encode('utf-8'))} bytes)")


if __name__ == "__main__":
    main()
