# -*- coding: utf-8 -*-

"""Validate API entries from README and optionally remove stale entries.

This script checks each API table row in README.md for:
1) Documentation/API link availability
2) A best-effort free-tier signal

If `--write` is enabled, rows that fail either check are removed from the file.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import List, Sequence, Tuple

from validate.links import check_if_link_is_working

FREE_TIER_KEYWORDS = (
    'free tier',
    'free plan',
    'free to use',
    'free api',
    'free',
    'public',
    'open',
    'no auth',
    'no api key',
    'without api key',
)


@dataclass
class ApiEntry:
    line_number: int
    raw_line: str
    title: str
    description: str
    auth: str
    link: str


def parse_api_entries(lines: Sequence[str]) -> List[ApiEntry]:
    """Parse README table rows that represent API entries."""
    entries: List[ApiEntry] = []

    for index, raw_line in enumerate(lines, start=1):
        line = raw_line.strip()

        if not line.startswith('| ['):
            continue

        segments = [segment.strip() for segment in line.split('|')]
        if len(segments) < 7:
            continue

        title_column = segments[1]
        description = segments[2]
        auth = segments[3]

        title_match = re.search(r'\[(.*?)\]', title_column)
        link_match = re.search(r'\((https?://[^)\s]+)\)', title_column)

        if not title_match or not link_match:
            continue

        entries.append(
            ApiEntry(
                line_number=index,
                raw_line=raw_line,
                title=title_match.group(1).strip(),
                description=description,
                auth=auth.strip('` ').lower(),
                link=link_match.group(1).strip(),
            )
        )

    return entries


def has_free_tier_signal(entry: ApiEntry) -> bool:
    """Best-effort free tier detector from metadata available in README."""
    desc = entry.description.lower()
    if entry.auth == 'no':
        return True

    for keyword in FREE_TIER_KEYWORDS:
        if keyword in desc:
            return True

    return False


def find_entries_to_remove(entries: Sequence[ApiEntry]) -> Tuple[List[ApiEntry], List[str]]:
    """Return API entries that should be removed and a human-readable report."""
    to_remove: List[ApiEntry] = []
    report: List[str] = []

    for entry in entries:
        link_has_error, link_error = check_if_link_is_working(entry.link)
        free_tier_ok = has_free_tier_signal(entry)

        reasons: List[str] = []

        if link_has_error:
            reasons.append(f'link check failed ({link_error})')

        if not free_tier_ok:
            reasons.append('no free-tier signal')

        if reasons:
            to_remove.append(entry)
            report.append(f'line {entry.line_number} - {entry.title}: {", ".join(reasons)}')

    return to_remove, report


def remove_entries_from_lines(lines: Sequence[str], entries_to_remove: Sequence[ApiEntry]) -> List[str]:
    remove_lines = {entry.line_number for entry in entries_to_remove}
    return [line for index, line in enumerate(lines, start=1) if index not in remove_lines]


def main(readme_path: str, write_changes: bool) -> int:
    path = Path(readme_path)
    lines = path.read_text(encoding='utf-8').splitlines()

    entries = parse_api_entries(lines)
    to_remove, report = find_entries_to_remove(entries)

    print(f'Checked {len(entries)} API entries.')

    if not to_remove:
        print('No entries flagged for removal.')
        return 0

    print(f'Flagged {len(to_remove)} entries for removal:')
    for item in report:
        print(f'- {item}')

    if write_changes:
        new_lines = remove_entries_from_lines(lines, to_remove)
        path.write_text('\n'.join(new_lines) + '\n', encoding='utf-8')
        print(f'Updated {readme_path} by removing {len(to_remove)} rows.')

    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check API rows and remove rows that fail link/free-tier checks.')
    parser.add_argument('filename', help='README file to validate')
    parser.add_argument('--write', action='store_true', help='Apply removals directly to file')
    args = parser.parse_args()

    raise SystemExit(main(args.filename, args.write))
