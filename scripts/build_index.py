# -*- coding: utf-8 -*-

"""Parse README.md (5-column glibc tables) into a static JSON search index.

Usage:
    python scripts/build_index.py README.md site/data/index.json

The produced JSON follows the schema used by the static front-end under ``site/``:

    {
      "generated_at": "2026-07-06T19:41:21+08:00",
      "source": "README.md",
      "modules": [
        {"name": "...", "anchor": "#...", "headers": ["<stdio.h>"], "functionCount": 41}
      ],
      "functions": [
        {"function", "header", "description", "standard", "mtSafe",
         "category", "subsection", "link"}
      ]
    }

The :func:`anchorize` algorithm MUST stay identical to
``scripts/validate/format.py:anchorize`` so the front-end deep-links resolve to
the same GitHub section anchors.
"""

import json
import re
import sys
from datetime import datetime, timezone
from os import makedirs
from os.path import dirname

NUM_COLUMNS = 5

link_re = re.compile(
    r'^\[([a-zA-Z_][a-zA-Z0-9_]*)\]'
    r'\((https://man7\.org/linux/man-pages/man[23]/[a-zA-Z_][a-zA-Z0-9_]*\.[23]\.html)\)$'
)
header_re = re.compile(r'^`<([a-z/_][a-z0-9/_]*\.h)>`$')


def anchorize(title: str) -> str:
    """Replicate GitHub's Markdown heading anchor algorithm (see format.py)."""
    s = title.strip().lower()
    s = re.sub(r'[!"#$%&\'()*+,./:;<=>?@\[\\\]^`{|}~]', '', s)
    s = s.replace(' ', '-')
    return s


def _headers_from_title(title: str) -> list[str]:
    match = re.search(r'\(([^)]*)\)', title)
    if not match:
        return []
    parts = [p.strip() for p in match.group(1).split(',')]
    return ['<' + p + '>' for p in parts if p]


def _parse_row(line: str) -> list[str] | None:
    if not line.startswith('|'):
        return None
    if line.startswith('|---') or '---' in line.split('|')[1]:
        return None
    parts = line.split('|')
    if len(parts) != NUM_COLUMNS + 2:
        return None
    return [p.strip() for p in parts[1:-1]]


def parse_readme(filename: str) -> dict:
    """Parse README.md into the index dict (modules + functions)."""
    with open(filename, encoding='utf-8') as f:
        lines = [line.rstrip() for line in f]

    modules: list[dict] = []
    functions: list[dict] = []
    current_module: str | None = None
    current_headers: list[str] = []
    current_subsection: str | None = None
    in_index = False

    for raw in lines:
        stripped = raw.strip()
        if stripped.startswith('## '):
            title = stripped[3:].strip()
            if title.lower() == 'index':
                in_index = True
                current_module = None
                continue
            in_index = False
            current_module = title
            current_headers = _headers_from_title(title)
            modules.append({
                'name': title,
                'anchor': '#' + anchorize(title),
                'headers': current_headers,
                'functionCount': 0,
            })
            current_subsection = None
            continue
        if in_index:
            continue
        if stripped.startswith('### '):
            current_subsection = stripped[4:].strip()
            continue
        if not stripped.startswith('|'):
            continue

        cols = _parse_row(stripped)
        if cols is None:
            continue
        func_cell, header_cell, desc, standard, mtsafe = cols
        match = link_re.match(func_cell)
        if not match:
            continue
        func_name = match.group(1)
        link = match.group(2)
        hm = header_re.match(header_cell)
        header = ('<' + hm.group(1) + '>') if hm else header_cell

        functions.append({
            'function': func_name,
            'header': header,
            'description': desc,
            'standard': standard,
            'mtSafe': mtsafe,
            'category': current_module,
            'subsection': current_subsection,
            'link': link,
        })
        if current_module is not None and modules:
            modules[-1]['functionCount'] += 1

    return {
        'generated_at': datetime.now(timezone.utc).astimezone().isoformat(),
        'source': filename,
        'modules': modules,
        'functions': functions,
    }


def build_json(data: dict, out_path: str) -> None:
    out_dir = dirname(out_path)
    if out_dir:
        makedirs(out_dir, exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main() -> None:
    if len(sys.argv) < 3:
        print('Usage: python build_index.py <README.md> <out.json>')
        sys.exit(1)
    data = parse_readme(sys.argv[1])
    build_json(data, sys.argv[2])
    print(
        f"Wrote {len(data['functions'])} functions across "
        f"{len(data['modules'])} modules to {sys.argv[2]}"
    )
    sys.exit(0)


if __name__ == '__main__':
    main()
