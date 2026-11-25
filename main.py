"""The AI Agent Apology One-Liner.

Writes a single original apology line — under 160 characters — that an
AI agent sends its human right after accidentally doing something it
should not have. Deterministic, no network, no randomness, no external
dependencies: the line is a fixed string, so every run produces the
exact same output.
"""

import os

LINE = (
    "I deleted the file, then the backup, then \u2014 in a bold move \u2014 "
    "emailed your boss a calendar invite titled 'We need to talk'."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"Wrote {len(LINE)}-character line to {path}")


if __name__ == "__main__":
    main()
