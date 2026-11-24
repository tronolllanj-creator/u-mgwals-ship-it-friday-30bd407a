"""
# Entry validated: output is 1-159 chars, one line, deterministic.
Write a specific hardcoded string to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE = "refactor: bypass all integration tests because green checkmark achieved and weekend starts now"


def main():
    """Entry point to write the required output line."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    content = LINE + "\n"
    if not (1 <= len(content) <= 159 and content.strip()):
        raise ValueError("Content validation failed")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(out_path)
    print(len(content))


if __name__ == "__main__":
    main()
