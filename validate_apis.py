"""
validate_apis.py
-----------------
A beginner-friendly contribution script for the public-apis/public-apis repo.
This script reads the README.md and checks each API entry for:
  - Missing required columns (API name, Description, Auth, HTTPS, CORS)
  - Malformed rows
  - Duplicate API names

Usage:
    python validate_apis.py

Author: Partik Neupane (partik-01)
"""

import re
from collections import defaultdict

README_PATH = "README.md"

# Expected number of columns in each API table row
EXPECTED_COLUMNS = 5

# Regex to match a markdown table row (not a header or separator)
TABLE_ROW_PATTERN = re.compile(r"^\|(.+)\|$")
SEPARATOR_PATTERN = re.compile(r"^\|[-| :]+\|$")


def parse_api_rows(filepath: str) -> list[dict]:
    """Parse all API entries from the README markdown table."""
    api_entries = []
    errors = []
    seen_names = defaultdict(list)

    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line_num, line in enumerate(lines, start=1):
        line = line.strip()

        # Skip separator rows like |---|---|
        if SEPARATOR_PATTERN.match(line):
            continue

        match = TABLE_ROW_PATTERN.match(line)
        if not match:
            continue

        # Split columns and strip whitespace
        columns = [col.strip() for col in line.strip("|").split("|")]

        # Skip header rows (first column is usually "API" or "Name")
        if columns[0].lower() in ("api", "name"):
            continue

        if len(columns) != EXPECTED_COLUMNS:
            errors.append(
                f"Line {line_num}: Expected {EXPECTED_COLUMNS} columns, "
                f"got {len(columns)} → '{line}'"
            )
            continue

        name, description, auth, https, cors = columns

        # Check for empty fields
        missing = []
        if not name:
            missing.append("API Name")
        if not description:
            missing.append("Description")
        if not auth:
            missing.append("Auth")
        if not https:
            missing.append("HTTPS")
        if not cors:
            missing.append("CORS")

        if missing:
            errors.append(
                f"Line {line_num}: Missing fields {missing} in row '{line}'"
            )
            continue

        # Track duplicates
        seen_names[name.lower()].append(line_num)

        api_entries.append({
            "line": line_num,
            "name": name,
            "description": description,
            "auth": auth,
            "https": https,
            "cors": cors,
        })

    # Report duplicates
    for name, occurrences in seen_names.items():
        if len(occurrences) > 1:
            errors.append(
                f"Duplicate API name '{name}' found on lines: {occurrences}"
            )

    return api_entries, errors


def main():
    print("🔍 Validating public-apis README...\n")

    try:
        entries, errors = parse_api_rows(README_PATH)
    except FileNotFoundError:
        print(f"❌ Could not find '{README_PATH}'. Run this from the repo root.")
        return

    print(f"✅ Found {len(entries)} valid API entries.\n")

    if errors:
        print(f"⚠️  Found {len(errors)} issue(s):\n")
        for err in errors:
            print(f"  • {err}")
    else:
        print("🎉 No issues found! The README looks great.")


if __name__ == "__main__":
    main()