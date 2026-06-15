# -*- coding: utf-8 -*-

import re
import sys

# 5 columns: Function | Header | Description | Standard | MT-Safe
NUM_COLUMNS = 5
MAX_DESC_LENGTH = 200

TABLE_HEADER = '| Function | Header | Description | Standard | MT-Safe |'
TABLE_SEPARATOR = '| --- | --- | --- | --- | --- |'

link_re = re.compile(r'^\[([a-zA-Z_][a-zA-Z0-9_]*)\]\(https://man7\.org/linux/man-pages/man[23]/[a-zA-Z_][a-zA-Z0-9_]*\.[23]\.html\)$')
header_re = re.compile(r'^`<[a-z/_][a-z0-9/_]*\.h>`$')
standard_re = re.compile(r'^[A-Za-z0-9._\-]+(, [A-Za-z0-9._\-]+)*(\s*\(.+\))?$')
mtsafe_re = re.compile(r'^(Yes|No)(\s*\(.+\))?$')


def error_message(line_number: int, message: str) -> str:
    line = line_number + 1
    return f'Line {line:4d}: {message}'


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


def check_file(filename: str) -> list[str]:
    errors = []

    with open(filename, mode='r', encoding='utf-8') as f:
        lines = [line.rstrip() for line in f]

    seen_header = False
    in_subsection = False  # Track if we are inside a ### subsection

    for line_num, line in enumerate(lines):
        stripped = line.strip()

        # Track section boundaries: reset state on any header
        if stripped.startswith('## ') or stripped.startswith('# ') or stripped.startswith('### '):
            seen_header = False
            in_subsection = stripped.startswith('### ')
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
                    errors.append(error_message(line_num, f'Expected {NUM_COLUMNS} columns, found {len(parts) - 2}: {stripped[:80]}'))
                continue

            if not seen_header:
                errors.append(error_message(line_num, f'Table data found without header: {stripped[:80]}'))
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
