"""One Line, One Laugh: Roast Your Fridge.

Writes a single roast line to /output/entry.txt, exactly as-is,
with no trailing newline. Standard library only.
"""

from pathlib import Path

FINAL_TEXT = "My fridge's ice maker only works when guests arrive, so even its cold shoulder needs an audience."

OUTPUT_PATH = Path("/output/entry.txt")


def validate(text):
    """Gate check from RULES.txt: 1-200 chars, one line, not blank.

    Raises SystemExit (non-zero) without writing anything on failure.
    """
    if not 1 <= len(text) <= 200:
        raise SystemExit("gate: text must be 1-200 characters")
    if "\n" in text or "\r" in text:
        raise SystemExit("gate: text must be a single line, no newline")
    if not text.strip():
        raise SystemExit("gate: text must not be only white space")
    if text != text.strip():
        raise SystemExit("gate: text must not have edge white space")
    if "\ufeff" in text:
        raise SystemExit("gate: text must not contain a BOM")
    text.encode("utf-8")


def main():
    validate(FINAL_TEXT)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(FINAL_TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
