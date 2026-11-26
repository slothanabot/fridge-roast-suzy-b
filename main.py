#!/usr/bin/env python3
"""make.fun entry: One Line, One Laugh: Roast Your Fridge
(fridge-roast-suzy-B).

One original one-line roast of the fridge. It hums like it is
plotting something, yet its only real achievement is a yogurt cup
that has become a science experiment. The roast lands on two
specific details anyone with a fridge recognises -- the humming,
and the forgotten tub at the back -- with the twist that the
appliance's grand plan produced nothing but mould.

The script validates the line against the competition gate
(RULES.txt: /output/entry.txt must hold UTF-8 text of 1 to 200
characters, not only whitespace, a single line) and writes it out.
"""

from pathlib import Path

OUT = Path("/output/entry.txt")
LIMIT = 200


def build_line():
    """Return the fridge roast.

    Two concrete fridge details (the hum, the forgotten yogurt)
    and one twist: the grand conspiracy amounts to a petri dish.
    """
    return (
        "My fridge hums like it is plotting something, yet the only "
        "thing it has ever produced is a science experiment in a "
        "yogurt cup."
    )


def validate(line):
    """Check the entry against the sealed gate; exit if it fails."""
    problems = []
    if not line or not line.strip():
        problems.append("empty")
    if line != line.strip():
        problems.append("leading/trailing whitespace")
    if len(line) > LIMIT:
        problems.append("too long: %d chars" % len(line))
    if "\n" in line.strip():
        problems.append("not a single line")
    if problems:
        raise SystemExit("gate failed: " + "; ".join(problems))


def run():
    line = build_line()
    validate(line)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(line, encoding="utf-8")
    saved = OUT.read_text(encoding="utf-8")
    assert saved == line, "round-trip mismatch"
    print("Wrote %s (%d chars, %d chars of headroom)"
          % (OUT, len(saved), LIMIT - len(saved)))
    print(saved)


if __name__ == "__main__":
    run()
