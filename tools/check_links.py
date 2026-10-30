"""Verify every internal markdown link and anchor in the design docs resolves.

The docs cross-reference each other heavily, so a renamed heading silently
breaks links. Run this after editing headings.

Usage:  py tools/check_links.py
"""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HEADING = re.compile(r"^#{1,6}\s+(.*)$", re.MULTILINE)


def slug(heading: str) -> str:
    """GitHub's heading-to-anchor rule, near enough for our purposes."""
    s = heading.strip().lower()
    s = re.sub(r"[`*_]", "", s)
    s = re.sub(r"[^\w\s-]", "", s)
    return re.sub(r"\s", "-", s)


def main() -> int:
    files = sorted(ROOT.rglob("*.md"))
    anchors = {
        f: {slug(h) for h in HEADING.findall(f.read_text(encoding="utf-8"))}
        for f in files
    }

    problems = []
    for f in files:
        for target in LINK.findall(f.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            path_part, _, anchor = target.partition("#")
            dest = (f.parent / path_part).resolve() if path_part else f
            if not dest.exists():
                problems.append(f"{f.name}: missing file -> {target}")
                continue
            if anchor and anchor not in anchors.get(dest, set()):
                problems.append(f"{f.name}: missing anchor -> {target}")

    for p in problems:
        print(p)
    checked = sum(len(LINK.findall(f.read_text(encoding='utf-8'))) for f in files)
    print(f"\n{len(files)} files, {checked} links, {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
