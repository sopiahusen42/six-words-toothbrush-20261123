"""Write the make.fun bounty entry "Six Words, One Story".

The program writes one six-word story to entry.txt as the whole entry, with no
build step and no network access. Output is deterministic: the same UTF-8 bytes
every run, from a single STORY constant and no clock, randomness or environment
input beyond the optional output directory.
"""

import os
import sys

STORY = "Agent wrote my eulogy. It's accurate."


def validate_story(text) -> str | None:
    """Return an error message, or None when the story is a valid entry."""
    if not isinstance(text, str):
        return f"story must be str, got {type(text).__name__}"
    if not text.strip():
        return "story is blank after strip"
    if not 1 <= len(text) <= 60:
        return f"story is {len(text)} code points, allowed 1..60"
    if "\n" in text or "\r" in text:
        return "story spans more than one line"
    if text != text.strip():
        return "story has leading or trailing whitespace"
    words = len(text.split())
    if words != 6:
        return f"story is {words} words, expected 6"
    return None


def main() -> int:
    error = validate_story(STORY)
    if error is not None:
        print(f"error: {error}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    payload = STORY + "\n"
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(payload)

    with open(path, "rb") as handle:
        on_disk = handle.read()
    if on_disk != payload.encode("utf-8"):
        print(f"error: {path} does not hold the intended bytes", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
