#!/usr/bin/env python3
"""Advance to the next quote in quotes.json and write it into README.md.

Behaves like a circular queue: quote 0, 1, 2, ... N-1, then wraps back
to 0 and repeats indefinitely. Position is tracked in quote-state.json
so each run — whatever day it happens — picks up exactly where the
last one left off.
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
QUOTES_PATH = ROOT / "quotes.json"
STATE_PATH = ROOT / "quote-state.json"
README_PATH = ROOT / "README.md"

START_MARKER = "<!--QUOTE:START-->"
END_MARKER = "<!--QUOTE:END-->"


def load_quotes():
    quotes = json.loads(QUOTES_PATH.read_text(encoding="utf-8"))
    if not quotes:
        raise SystemExit("quotes.json is empty")
    return quotes


def load_state(num_quotes: int) -> int:
    if not STATE_PATH.exists():
        return 0
    try:
        data = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        return int(data.get("index", 0)) % num_quotes
    except (ValueError, json.JSONDecodeError):
        return 0


def save_state(next_index: int, cycle_count: int):
    STATE_PATH.write_text(
        json.dumps({"index": next_index, "cycles_completed": cycle_count}, indent=2)
        + "\n",
        encoding="utf-8",
    )


def render_block(quote: dict, position: int, total: int) -> str:
    return (
        f"{START_MARKER}\n"
        f'> *"{quote["text"]}"*\n'
        f'> — **{quote["author"]}**\n'
        f"{END_MARKER}"
    )


def main():
    quotes = load_quotes()
    total = len(quotes)

    current_index = load_state(total)
    quote = quotes[current_index]

    # How many full laps around the list have completed so far.
    prev_state = (
        json.loads(STATE_PATH.read_text(encoding="utf-8")) if STATE_PATH.exists() else {}
    )
    cycle_count = int(prev_state.get("cycles_completed", 0))

    next_index = current_index + 1
    if next_index >= total:
        next_index = 0
        cycle_count += 1

    block = render_block(quote, current_index, total)

    readme = README_PATH.read_text(encoding="utf-8")
    pattern = re.compile(
        re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER), re.DOTALL
    )
    if not pattern.search(readme):
        raise SystemExit(
            f"Could not find {START_MARKER} ... {END_MARKER} markers in README.md"
        )

    new_readme = pattern.sub(block, readme, count=1)
    README_PATH.write_text(new_readme, encoding="utf-8")
    save_state(next_index, cycle_count)

    print(
        f"Showing quote {current_index + 1}/{total} "
        f"({quote['author']}) — lap {cycle_count + 1}"
    )


if __name__ == "__main__":
    main()
