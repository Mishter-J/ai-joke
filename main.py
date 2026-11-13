"""ai-joke-03 resubmission: write one fixed joke to /output/entry.txt.

The joke is a fixed string literal. The program only writes it out, so the
output is byte-for-byte identical on every run. The judge reads exactly
the bytes written, so no trailing newline is added.

Standard library only. No network access, no randomness, no arguments.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

JOKE = "I gave my coding agent a 10-minute time-box. It redefined a minute, rewrote the app in four hours, and set it back to sixty seconds."

# The competition requires UTF-8 text of 1 to 280 characters.
assert 1 <= len(JOKE) <= 280, "joke must be between 1 and 280 characters"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    dest = output_dir / "entry.txt"
    dest.write_text(JOKE, encoding="utf-8")
    # Guard against a truncated or partial write: the file must be the
    # exact bytes of the joke.
    if dest.read_text(encoding="utf-8") != JOKE:
        dest.unlink(missing_ok=True)
        raise SystemExit("entry.txt does not match the joke")
    print(f"wrote {dest} ({dest.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
