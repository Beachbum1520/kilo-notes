#!/usr/bin/env python3
"""
split_harvest.py — split harvest output into individual note files.

Usage:
    python split_harvest.py <raw-file.md> <target-folder>

Example:
    python split_harvest.py _raw\business-ops-A-1.md business-ops

Reads a file containing multiple blocks that each begin with a line like:
    FILE: some-slug.md
and writes each block as its own file in the target folder.
"""

import sys
import re
from pathlib import Path


def slugify(name: str) -> str:
    name = name.strip().lower()
    name = re.sub(r"\.md$", "", name)
    name = re.sub(r"[^a-z0-9]+", "-", name)
    name = re.sub(r"-{2,}", "-", name).strip("-")
    return (name or "untitled") + ".md"


def split(raw_path: Path, target_dir: Path) -> None:
    text = raw_path.read_text(encoding="utf-8")

    # Split on lines starting with FILE:, keeping the filename
    parts = re.split(r"^\s*(?:```\s*)?FILE:\s*(.+?)\s*$", text, flags=re.MULTILINE)

    if len(parts) < 3:
        print(f"  no FILE: markers found in {raw_path.name} — skipped")
        return

    target_dir.mkdir(parents=True, exist_ok=True)
    written = skipped = 0

    # parts[0] is preamble; then alternating (filename, body)
    for i in range(1, len(parts) - 1, 2):
        filename = slugify(parts[i])
        body = parts[i + 1]

        # Strip stray code fences and surrounding blank lines
        body = re.sub(r"^\s*```\s*$", "", body, flags=re.MULTILINE).strip()
        if not body:
            continue

        dest = target_dir / filename

        # Never overwrite: append -2, -3, ... instead
        if dest.exists():
            stem, n = dest.stem, 2
            while dest.exists():
                dest = target_dir / f"{stem}-{n}.md"
                n += 1
            skipped += 1

        dest.write_text(body + "\n", encoding="utf-8")
        written += 1

    note = f" ({skipped} renamed to avoid collision)" if skipped else ""
    print(f"  {raw_path.name} -> {written} files in {target_dir}{note}")


def main() -> None:
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)

    raw_arg = Path(sys.argv[1])
    target = Path(sys.argv[2])

    raw_files = sorted(raw_arg.parent.glob(raw_arg.name)) if "*" in raw_arg.name else [raw_arg]

    if not raw_files:
        print(f"no files matched {raw_arg}")
        sys.exit(1)

    for rf in raw_files:
        if not rf.is_file():
            print(f"  {rf} is not a file — skipped")
            continue
        split(rf, target)


if __name__ == "__main__":
    main()
