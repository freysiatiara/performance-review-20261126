"""Funniest One-Line Performance Review — make.fun entry.

Writes a single-line performance review (an AI agent reviewing its
human operator) to the output path, with no trailing newline.
Stdlib only.
"""

import os

ENTRY = (
    "Promotion approved: after years of training me to do his job, "
    "he has finally made himself redundant."
)


def resolve_output_path():
    """Resolve the output path: ENTRY_OUTPUT, then OUTPUT_DIR /
    MAKEFUN_OUTPUT_DIR, then the default /output/entry.txt."""
    direct = os.environ.get("ENTRY_OUTPUT")
    if direct:
        return direct
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        base = os.environ.get(var)
        if base:
            return os.path.join(base, "entry.txt")
    return "/output/entry.txt"


def main():
    # Validation guard: the gate requires UTF-8 text of 1..140
    # characters, not only whitespace, and exactly one line.
    text = ENTRY
    assert isinstance(text, str)
    assert 1 <= len(text) <= 140, "entry must be 1..140 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    text.encode("utf-8")

    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
