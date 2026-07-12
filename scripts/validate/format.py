# -*- coding: utf-8 -*-

import re
import sys

# 5 columns: Function | Header | Description | Standard | MT-Safe
NUM_COLUMNS = 5
MAX_DESC_LENGTH = 200
MIN_DESC_LENGTH = 10

TABLE_HEADER = '| Function | Header | Description | Standard | MT-Safe |'
TABLE_SEPARATOR = '| --- | --- | --- | --- | --- |'

# 标准列中一旦出现这些词，说明该函数已从标准中移除/废弃，
# 对应描述应显式标注 (deprecated)，否则读者容易误用。
OBSOLETE_STANDARD_HINTS = ('removed', 'deprecated', 'obsolete')

link_re = re.compile(r'^\[([a-zA-Z_][a-zA-Z0-9_]*)\]\(https://man7\.org/linux/man-pages/man[23]/[a-zA-Z_][a-zA-Z0-9_]*\.[23]\.html\)$')
# 仅提取函数名（用于字母序检查）
func_name_re = re.compile(r'^\[([a-zA-Z_][a-zA-Z0-9_]*)\]')
header_re = re.compile(r'^`<[a-z/_][a-z0-9/_]*\.h>`$')
standard_re = re.compile(r'^[A-Za-z0-9._\-]+(, [A-Za-z0-9._\-]+)*(\s*\(.+\))?$')
mtsafe_re = re.compile(r'^(Yes|No)(\s*\(.+\))?$')


def error_message(line_number: int, message: str) -> str:
    line = line_number + 1
    return f'Line {line:4d}: {message}'


def warning_message(line_number: int, message: str) -> str:
    line = line_number + 1
    return f'Line {line:4d}: [warn] {message}'


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


def check_alphabetical_order(func_names: list[str]) -> list[int]:
    """Return the indices of entries that violate strict ASCII ascending order
    within a single subsection. Migrated from upstream public-apis maintenance
    discipline: entries must be sorted alphabetically so the index stays scannable.

    Returns a list of indices ``i`` where ``func_names[i] < func_names[i-1]``.
    """
    out_of_order = []
    for i in range(1, len(func_names)):
        if func_names[i] < func_names[i - 1]:
            out_of_order.append(i)
    return out_of_order


def check_file(filename: str) -> tuple[list[str], list[str]]:
    """Validate the README tables.

    Returns a tuple ``(errors, warnings)``. ``errors`` are fatal (non-zero exit),
    ``warnings`` are non-blocking advisory checks migrated from upstream
    public-apis maintenance practice.
    """
    errors: list[str] = []
    warnings: list[str] = []

    with open(filename, mode='r', encoding='utf-8') as f:
        lines = [line.rstrip() for line in f]

    seen_header = False
    in_subsection = False
    current_subsection: str | None = None
    # (func_name, line_num) accumulated within the current ### subsection
    subsection_funcs: list[tuple[str, int]] = []

    def flush_subsection() -> None:
        nonlocal subsection_funcs
        if subsection_funcs:
            names = [n for n, _ in subsection_funcs]
            for i in check_alphabetical_order(names):
                prev, cur = names[i - 1], names[i]
                ln = subsection_funcs[i][1]
                warnings.append(
                    warning_message(
                        ln,
                        f"'{cur}' should come before '{prev}' "
                        f"(subsection '{current_subsection}' not in alphabetical order)",
                    )
                )
        subsection_funcs = []

    for line_num, line in enumerate(lines):
        stripped = line.strip()

        # Section/subsection boundaries reset table state
        if stripped.startswith('## ') or stripped.startswith('# ') or stripped.startswith('### '):
            flush_subsection()
            seen_header = False
            in_subsection = stripped.startswith('### ')
            current_subsection = stripped[4:].strip() if in_subsection else None
            continue

        # Skip empty lines, horizontal rules, <br> etc
        if stripped == '' or stripped == '---' or stripped == '<br>':
            continue

        # Check if it's a table header row
        if is_table_header(stripped):
            flush_subsection()
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

            # Check each column (fatal)
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

            # --- Migrated upstream-maintenance checks (warnings, non-fatal) ---

            # 描述深度统一：过短的描述提示补充（参考上游 BuyWhere 补齐描述的实践）
            if 0 < len(desc) < MIN_DESC_LENGTH:
                warnings.append(
                    warning_message(
                        line_num,
                        f'Description is very short ({len(desc)} chars); prefer a fuller '
                        f'sentence covering function, key args, and return/errors',
                    )
                )

            # 死条目/废弃标注：标准标注 removed/deprecated 时，描述应显式说明废弃
            if any(h in standard.lower() for h in OBSOLETE_STANDARD_HINTS):
                dl = desc.lower()
                if not ('deprecat' in dl or 'removed' in dl or 'obsolete' in dl):
                    warnings.append(
                        warning_message(
                            line_num,
                            'Standard marks this as removed/deprecated; Description should '
                            'state "(deprecated) ..." so readers are warned',
                        )
                    )

            # 字母序累积
            m = func_name_re.match(func)
            if m and in_subsection:
                subsection_funcs.append((m.group(1), line_num))

    flush_subsection()
    return errors, warnings


def main() -> None:
    if len(sys.argv) < 2:
        print('Usage: python format.py <file.md>')
        sys.exit(1)

    filename = sys.argv[1]
    errors, warnings = check_file(filename)

    if errors:
        print(f'Found {len(errors)} format error(s) in {filename}:')
        for err in errors:
            print(f'  - {err}')
    if warnings:
        print(f'Found {len(warnings)} format warning(s) (non-blocking):')
        for w in warnings:
            print(f'  - {w}')

    if errors:
        sys.exit(1)
    elif warnings:
        print(f'{filename}: format OK ({len(warnings)} warning(s))')
        sys.exit(0)
    else:
        print(f'{filename}: format OK')
        sys.exit(0)


if __name__ == '__main__':
    main()
