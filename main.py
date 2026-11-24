"""Angry Judge: The Short Rant Contest entry.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt. The rant is a fixed text composed for this entry:
the hotel shower with exactly two temperatures and no middle ground.

What the rant is judged on, and how this entry targets each criterion:

- It must be short. One compact paragraph, well under the 400-character
  ceiling, so the whole rant lands in a single breath.
- It must be funny. The shower's two settings are exaggerated into
  arctic blast and molten lava, and the useless knob in between is
  called decorative — the joke is the impossibility of a comfortable
  temperature, not the plumbing itself.
- It must feel real. "I have done the research" and the small dance of
  regret put a specific person in the scene instead of a generic
  complaint, so the annoyance reads as lived experience.
- It must be vivid. The closing image — the water laughing in a
  language the speaker doesn't speak — gives the rant a memorable
  last line rather than trailing off on the complaint.

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


def _check_length(text):
    """Length gate: the rant must be non-blank text of 1-400 characters."""
    if not isinstance(text, str):
        return False
    if not text.strip():
        return False
    return 1 <= len(text) <= 400


def _check_content(text):
    """Content gate: the text must encode cleanly as UTF-8."""
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def validate(text):
    """Check the rant against the gate: length first, then content."""
    return _check_length(text) and _check_content(text)


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
