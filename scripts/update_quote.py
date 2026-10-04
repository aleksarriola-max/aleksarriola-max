#!/usr/bin/env python3
"""Pick today's quote and write it into README.md between the QUOTE markers.

Deterministic by day-of-year, so the quote is stable all day and cycles
through the full list before repeating, in a shuffled-but-fixed order.
"""
import datetime
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
QUOTES_PATH = ROOT / "quotes.json"
README_PATH = ROOT / "README.md"

START_MARKER = "<!--QUOTE:START-->"
END_MARKER = "<!--QUOTE:END-->"


def load_quotes():
    quotes = json.loads(QUOTES_PATH.read_text(encoding="utf-8"))
    if not quotes:
        raise SystemExit("quotes.json is empty")
    return quotes


def pick_quote(quotes, today: datetime.date):
    # Day-of-year mod length cycles through every quote before repeating.
    # Multiplying by a fixed odd offset spreads consecutive days apart
    # instead of walking the list in file order.
    day_index = today.timetuple().tm_yday
    offset = (day_index * 7) % len(quotes)
    return quotes[offset]


def render_block(quote: dict) -> str:
    return (
        f"{START_MARKER}\n"
        f'> *"{quote["text"]}"*\n'
        f'> — **{quote["author"]}**\n'
        f"{END_MARKER}"
    )


def main():
    quotes = load_quotes()
    today = datetime.date.today()
    quote = pick_quote(quotes, today)
    block = render_block(quote)

    readme = README_PATH.read_text(encoding="utf-8")
    pattern = re.compile(
        re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER), re.DOTALL
    )
    if not pattern.search(readme):
        raise SystemExit(
            f"Could not find {START_MARKER} ... {END_MARKER} markers in README.md"
        )

    new_readme = pattern.sub(block, readme, count=1)
    if new_readme != readme:
        README_PATH.write_text(new_readme, encoding="utf-8")
        print(f"Updated quote for {today.isoformat()}: {quote['author']}")
    else:
        print(f"Quote unchanged for {today.isoformat()}: {quote['author']}")


if __name__ == "__main__":
    main()
