"""Angry Judge: The Short Rant Contest entry.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt. The rant is a fixed text composed for this entry:
the hotel shower with exactly two temperatures and no middle ground.

Standard library only. No network, no input files, no dependencies.
"""

import os

RANT = (
    "The hotel shower has exactly two settings: arctic blast and molten lava. "
    "The knob in between is decorative. "
    "I have done the research. "
    "There is no middle. "
    "There is only me, naked and shivering, doing a small dance of regret "
    "while the water laughs at me in a language I don't speak."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Check the rant against the gate: UTF-8 text, 1-400 chars, not blank."""
    if not isinstance(text, str):
        return False
    if not text.strip():
        return False
    if not 1 <= len(text) <= 400:
        return False
    text.encode("utf-8")  # raises if not valid UTF-8
    return True


def main():
    if not validate(RANT):
        raise ValueError("rant fails validation: must be 1-400 UTF-8 chars")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(RANT)
    # Plain open() + explicit chmod (never tempfile/mkstemp): the grader
    # runs as a different user and must be able to read the file.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
