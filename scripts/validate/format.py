# -*- coding: utf-8 -*-

"""Validate the 5-column glibc function tables inside README.md.

Schema:  Function | Header | Description | Standard | MT-Safe

This module performs two kinds of checks:

* Column-level checks (existing): verify each table row conforms to the 5-column
  schema (link format, header format, description case/length, standard, MT-Safe).
* Content-level checks (T04): duplicate function names within a module, Index <-> module
  heading anchor synchronisation, and MT-Safe value consistency.

Errors block the build (non-zero exit code). Warnings are printed but never block.
"""

import re
import sys

# 5 columns: Function | Header | Description | Standard | MT-Safe
NUM_COLUMNS = 5
MAX_DESC_LENGTH = 200

TABLE_HEADER = '| Function | Header | Description | Standard | MT-Safe |'
TABLE_SEPARATOR = '| --- | --- | --- | --- | --- |'

link_re = re.compile(
    r'^\[([a-zA-Z_][a-zA-Z0-9_]*)\]'
    r'\((https://man7\.org/linux/man-pages/man[23]/[a-zA-Z_][a-zA-Z0-9_]*\.[23]\.html)\)$'
)
header_re = re.compile(r'^`<[a-z/_][a-z0-9/_]*\.h>`$')
standard_re = re.compile(r'^[A-Za-z0-9._\-]+(, [A-Za-z0-9._\-]+)*(\s*\(.+\))?$')
mtsafe_re = re.compile(r'^(Yes|No)(\s*\(.+\))?$')


def error_message(line_number: int, message: str) -> str:
    """Format an error message with a 1-based, 4-wide line number."""
    line = line_number + 1
    return f'Line {line:4d}: {message}'


def anchorize(title: str) -> str:
    """Replicate GitHub's Markdown heading anchor algorithm.

    GitHub generates the slug from the *raw* heading source: it lower-cases the
    text, strips punctuation (``&`` included), and replaces spaces with single
    hyphens. Critically, GitHub does **not** decode HTML entities before
    slugifying, so a heading written as ``Environment &amp; System Info`` yields
    the slug ``environment-amp-system-info-...`` which diverges from the ``&``
    based anchor used in the Index. Always write headings with a literal ``&``.

    This exact algorithm is shared with ``scripts/build_index.py`` so that the
    static front-end deep-links resolve to the same GitHub section anchors.
    """
    s = title.strip().lower()
    s = re.sub(r'[!"#$%&\'()*+,./:;<=>?@\[\\\]^`{|}~]', '', s)
    s = s.replace(' ', '-')
    return s


def check_function_column(func: str) -> str | None:
    if not link_re.match(func):
        return f'Function column must be [name](https://man7.org/...) link, got: {func}'
    return None


def check_header_column(header: str) -> str | None:
    if not header_re.match(header):
        return f'Header column must be `<header.h>` format, got: {header}'
    return None


def check_description_column(desc: str) -> str | None:
    if len(desc) == 0:
        return 'Description is empty'
    if not desc[0].isupper() and not desc[0].isdigit():
        return f'Description should start with uppercase letter, got: {desc[:30]}...'
    if len(desc) > MAX_DESC_LENGTH:
        return f'Description exceeds {MAX_DESC_LENGTH} characters (has {len(desc)})'
    return None


def check_standard_column(standard: str) -> str | None:
    if not standard_re.match(standard):
        return f'Standard column format is invalid, got: {standard}'
    return None


def check_mtsafe_column(mtsafe: str) -> str | None:
    if not mtsafe_re.match(mtsafe):
        return f'MT-Safe column must be Yes or No (optionally with note in parentheses), got: {mtsafe}'
    return None


def parse_line(line: str) -> list[str] | None:
    """Parse a table data row, returning stripped column values, or None if not a data row."""
    if not line.startswith('|'):
        return None
    if line.startswith('|---') or '---' in line.split('|')[1] or TABLE_HEADER in line:
        return None
    parts = line.split('|')
    if len(parts) != NUM_COLUMNS + 2:
        return None
    return [p.strip() for p in parts[1:-1]]


def is_table_header(line: str) -> bool:
    return line.strip() == TABLE_HEADER


def is_table_separator(line: str) -> bool:
    return line.strip() == TABLE_SEPARATOR


def check_duplicate_functions(lines: list[str]) -> tuple[list[str], list[str]]:
    """Check for duplicate function names within the same module.

    Returns ``(errors, warnings)``. A function name that appears more than once
    inside the same ``## Module`` section is an **error**. The same function name
    appearing across different modules is allowed (intentional cross-module reuse,
    e.g. ``strerror``/``dup2``) and produces no message.
    """
    errors: list[str] = []
    warnings: list[str] = []
    current_module: str | None = None
    seen: dict[str, int] = {}

    for line_number, raw in enumerate(lines):
        stripped = raw.strip()
        if stripped.startswith('## '):
            title = stripped[3:].strip()
            if title.lower() == 'index':
                current_module = None
            else:
                current_module = title
                seen = {}
            continue
        if stripped.startswith('#') or not stripped.startswith('|'):
            continue

        cols = parse_line(stripped)
        if cols is None:
            continue
        func_cell = cols[0]
        match = link_re.match(func_cell)
        if not match:
            continue
        func_name = match.group(1)
        if current_module is None:
            continue
        if func_name in seen:
            errors.append(
                error_message(
                    line_number,
                    f'Duplicate function "{func_name}" in module "{current_module}"',
                )
            )
        else:
            seen[func_name] = 1
    return errors, warnings


def _extract_index_anchors(lines: list[str]) -> list[str]:
    """Extract the anchor portion of every ``* [Text](#anchor)`` bullet in the Index."""
    anchors: list[str] = []
    in_index = False
    pattern = re.compile(r'^\*\s*\[[^\]]*\]\(#([a-z0-9\-]+)\)')
    for raw in lines:
        stripped = raw.strip()
        if stripped.startswith('## '):
            in_index = stripped[3:].strip().lower() == 'index'
            continue
        if not in_index:
            continue
        match = pattern.match(stripped)
        if match:
            anchors.append(match.group(1))
    return anchors


def _extract_module_slugs(lines: list[str]) -> list[str]:
    """Compute the anchor slug for every ``## Module`` heading (Index excluded)."""
    slugs: list[str] = []
    for raw in lines:
        stripped = raw.strip()
        if stripped.startswith('## '):
            title = stripped[3:].strip()
            if title.lower() == 'index':
                continue
            slugs.append(anchorize(title))
    return slugs


def check_index_sync(lines: list[str]) -> list[str]:
    """Verify the Index anchor set matches the set of module heading slugs.

    The Index section lists ``* [Name](#anchor)`` links; each anchor must
    correspond to exactly one ``## Module`` heading slug (computed from the raw
    heading text with :func:`anchorize`). When a module heading uses an HTML
    entity such as ``&amp;`` the raw slug diverges from the Index anchor, which is
    exactly the broken-link bug this check is designed to catch.
    """
    errors: list[str] = []
    anchors = _extract_index_anchors(lines)
    slugs = _extract_module_slugs(lines)
    anchor_set = set(anchors)
    slug_set = set(slugs)

    if anchor_set != slug_set:
        missing = slug_set - anchor_set  # modules without an Index entry
        extra = anchor_set - slug_set    # Index entries without a module
        if missing:
            errors.append(
                'Index is missing entries for module(s): ' + ', '.join(sorted(missing))
            )
        if extra:
            errors.append(
                'Index contains entries not matching any module: '
                + ', '.join(sorted(extra))
            )
    if len(anchors) != len(set(anchors)):
        errors.append('Index contains duplicate anchors')
    return errors


def check_mtsafe_consistency(lines: list[str]) -> list[str]:
    """Warn when the same function name is annotated with conflicting MT-Safe values.

    Returns a list of warning messages. This check is non-blocking (warnings only).
    """
    warnings: list[str] = []
    by_name: dict[str, set[str]] = {}
    for raw in lines:
        stripped = raw.strip()
        if not stripped.startswith('|') or stripped.startswith('|---'):
            continue
        cols = parse_line(stripped)
        if cols is None:
            continue
        func_cell, _, _, _, mtsafe = cols
        match = link_re.match(func_cell)
        if not match:
            continue
        func_name = match.group(1)
        by_name.setdefault(func_name, set()).add(mtsafe)

    for func_name, values in by_name.items():
        if len(values) > 1:
            warnings.append(
                f'MT-Safe inconsistent for "{func_name}": ' + ' vs '.join(sorted(values))
            )
    return warnings


def check_file(filename: str) -> list[str]:
    """Validate a Markdown file and return a list of blocking errors.

    Warnings (e.g. MT-Safe inconsistencies) are printed to stdout but are not
    returned, so they never cause a non-zero exit code.
    """
    errors: list[str] = []
    warnings: list[str] = []

    with open(filename, mode='r', encoding='utf-8') as f:
        lines = [line.rstrip() for line in f]

    seen_header = False

    for line_num, line in enumerate(lines):
        stripped = line.strip()

        # Track section boundaries: reset state on any header
        if stripped.startswith('## ') or stripped.startswith('# ') or stripped.startswith('### '):
            seen_header = False
            continue

        # Skip empty lines, horizontal rules, <br> etc
        if stripped == '' or stripped == '---' or stripped == '<br>':
            continue

        # Check if it's a table header row
        if is_table_header(stripped):
            if seen_header:
                errors.append(error_message(line_num, 'Duplicate table header'))
            seen_header = True
            continue

        # Check if it's a table separator row
        if is_table_separator(stripped):
            if not seen_header:
                errors.append(error_message(line_num, 'Table separator found before header'))
            continue

        # Parse table data rows
        if stripped.startswith('|'):
            cols = parse_line(stripped)
            if cols is None:
                # Still a |...| line but wrong column count or structure
                parts = stripped.split('|')
                if len(parts) != NUM_COLUMNS + 2:
                    errors.append(error_message(
                        line_num,
                        f'Expected {NUM_COLUMNS} columns, found {len(parts) - 2}: {stripped[:80]}',
                    ))
                continue

            if not seen_header:
                errors.append(error_message(
                    line_num, f'Table data found without header: {stripped[:80]}'))
                continue

            func, header, desc, standard, mtsafe = cols

            # Check each column
            err = check_function_column(func)
            if err:
                errors.append(error_message(line_num, err))

            err = check_header_column(header)
            if err:
                errors.append(error_message(line_num, err))

            err = check_description_column(desc)
            if err:
                errors.append(error_message(line_num, err))

            err = check_standard_column(standard)
            if err:
                errors.append(error_message(line_num, err))

            err = check_mtsafe_column(mtsafe)
            if err:
                errors.append(error_message(line_num, err))

    # --- Content-level checks (T04) ---
    dup_errors, dup_warnings = check_duplicate_functions(lines)
    errors.extend(dup_errors)
    warnings.extend(dup_warnings)

    errors.extend(check_index_sync(lines))
    warnings.extend(check_mtsafe_consistency(lines))

    # Warnings are informational only and must not block the build.
    for warning in warnings:
        print(f'WARNING: {warning}')

    return errors


def main() -> None:
    if len(sys.argv) < 2:
        print('Usage: python format.py <file.md>')
        sys.exit(1)

    filename = sys.argv[1]
    errors = check_file(filename)

    if errors:
        print(f'Found {len(errors)} format issue(s) in {filename}:')
        for err in errors:
            print(f'  - {err}')
        sys.exit(1)
    else:
        print(f'{filename}: format OK')
        sys.exit(0)


if __name__ == '__main__':
    main()
