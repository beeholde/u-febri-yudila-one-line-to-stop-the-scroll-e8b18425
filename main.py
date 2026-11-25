# One Line to Stop the Scroll — u-febri-yudila-one-line-to-stop-the-scroll-e8b18425
# makefun anchor d95beac534eaea879deb016e364e3a6068d6442c round 34257005
# Writes a single line to /output/entry.txt: a stranger's wave, answered
# by mistake, and both sides committing to it. Stdlib only, deterministic,
# no trailing newline.
import os

LINE = "I waved back at a stranger who was waving at someone behind me, and we both committed to it for a full three seconds."

# Gate: entry must be 1-200 chars of UTF-8 text, not whitespace-only.
MAX_CHARS = 200
assert 1 <= len(LINE) <= MAX_CHARS and LINE.strip(), "line outside 1-200 chars"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
