"""Write the two-line everyday-things entry to /output/entry.txt.

Line 1 explains a queue to a 10-year-old through a single analogy:
a caterpillar made of people, standing in single file and wiggling
forward one step at a time.

Line 2 is honest about that analogy: it says what the caterpillar
maps (the single-file line, the slow forward wiggle) and what it
leaves out (boredom, cutting in line, leaving and coming back).
"""

import os

# The entry is exactly two lines, one sentence each, and must stay
# inside the bounty gate of 1 to 400 UTF-8 characters, with no
# trailing newline, so the judge sees the pair exactly as written.
ENTRY = (
    "A queue is a caterpillar made of people: everyone stands behind "
    "the person in front, and the whole line wiggles forward one step "
    "at a time.\n"
    "The caterpillar maps the single-file line and the slow forward "
    "wiggle, but it leaves out that a real caterpillar never gets "
    "bored, never cuts in line, and never leaves to come back later."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path}: {len(ENTRY)} chars")


if __name__ == "__main__":
    main()
