#!/usr/bin/env python3
"""Write the latest essays from the portfolio's RSS feed into README.md.

Reads https://aleksarriola-max.github.io/feed.xml (or a local file passed as
the first argument) and replaces the block between the ESSAYS markers with
the newest three essays. Leaves the README untouched if the feed can't be
read, so a temporary outage never blanks the section.
"""
import sys
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from pathlib import Path

FEED_URL = "https://aleksarriola-max.github.io/feed.xml"
README = Path(__file__).resolve().parent.parent / "README.md"
START, END = "<!--ESSAYS:START-->", "<!--ESSAYS:END-->"
COUNT = 3


def load_feed(source: str) -> bytes:
    if source.startswith("http"):
        req = urllib.request.Request(source, headers={"User-Agent": "profile-readme-bot"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            return resp.read()
    return Path(source).read_bytes()


def main() -> int:
    source = sys.argv[1] if len(sys.argv) > 1 else FEED_URL
    try:
        root = ET.fromstring(load_feed(source))
    except Exception as exc:  # network or parse error: keep the old list
        print(f"Feed unavailable ({exc}); README left unchanged.")
        return 0

    items = []
    for item in root.iter("item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        try:
            date = parsedate_to_datetime(item.findtext("pubDate") or "")
        except Exception:
            continue
        if title and link:
            items.append((date, title, link))
    items.sort(key=lambda x: x[0], reverse=True)
    if not items:
        print("Feed had no essays; README left unchanged.")
        return 0

    lines = [f"- [{t}]({l}) · {d.strftime('%b')} {d.day}" for d, t, l in items[:COUNT]]
    block = START + "\n" + "\n".join(lines) + "\n" + END

    text = README.read_text(encoding="utf-8")
    if START not in text or END not in text:
        print("ESSAYS markers not found in README.md")
        return 1
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    new = head + block + tail
    if new != text:
        README.write_text(new, encoding="utf-8")
        print(f"Updated latest essays: {items[0][1]}")
    else:
        print("Latest essays already current.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
