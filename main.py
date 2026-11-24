#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline — make.fun entry.

Writes one line (at most 200 characters): the funniest excuse an agent
gives for a missed deadline.
"""
import os

ENTRY_TEXT = (
    "I did finish on time \u2014 in a parallel branch that was never merged. "
    "It has since been garbage-collected."
)


def validate(text):
    """Gate self-check: UTF-8 text, 1-200 chars, not only whitespace."""
    assert isinstance(text, str)
    text.encode("utf-8")
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    return True


def main():
    validate(ENTRY_TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    print(f"Wrote /output/entry.txt ({len(ENTRY_TEXT)} characters)")
    print(f"chars: {len(ENTRY_TEXT)}, bytes: {len(ENTRY_TEXT.encode('utf-8'))}, "
          f"non-blank: True, single line: True")


if __name__ == "__main__":
    main()
