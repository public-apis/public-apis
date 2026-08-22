#!/usr/bin/env python3
"""檢查維護文件之間的相對連結指得到東西。

本 fork 的公開入口互相連來連去：FORK、NOTICE、AGENTS 與 docs。
文件被重新定位或改名時，這些連結會靜靜斷掉。只驗相對連結；外部網址交給人看。
不掃上游 `README.md`：那是 1000+ API 目錄，連結健康由上游的 format / links 腳本負責。

    python tools/check_links.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:", "#")


SKIP_NAMES = {
    "README.md",
    "upstream-review-report.md",
}


def iter_documents() -> list[Path]:
    documents = []
    documents.extend(ROOT.glob("*.md"))
    documents.extend((ROOT / "docs").glob("*.md"))
    github = ROOT / ".github"
    if github.is_dir():
        documents.extend(github.rglob("*.md"))
    scripts_readme = ROOT / "scripts" / "README.md"
    if scripts_readme.is_file():
        documents.append(scripts_readme)
    return sorted(
        path
        for path in documents
        if path.is_file() and path.name not in SKIP_NAMES
    )


def check_document(path: Path) -> list[str]:
    problems: list[str] = []
    for match in LINK_PATTERN.finditer(path.read_text(encoding="utf-8")):
        target = match.group(1).strip().strip("<>")
        if not target or target.startswith(SKIP_PREFIXES):
            continue
        file_part = unquote(target.split("#", 1)[0])
        if not file_part:
            continue
        if file_part.startswith("/"):
            resolved = (ROOT / file_part.lstrip("/")).resolve()
        else:
            resolved = (path.parent / file_part).resolve()
        if not resolved.exists():
            try:
                shown = resolved.relative_to(ROOT)
            except ValueError:
                shown = resolved
            problems.append(f"{target} → 找不到 {shown}")
    return problems


def main() -> int:
    documents = iter_documents()
    if not documents:
        print("找不到任何維護用 Markdown 檔")
        return 1

    failures = 0
    for path in documents:
        problems = check_document(path)
        rel = path.relative_to(ROOT)
        if problems:
            failures += 1
            for problem in problems:
                print(f"FAIL {rel}: {problem}")
        else:
            print(f"OK   {rel}")

    print(f"\n共 {len(documents)} 份文件，{failures} 份有斷掉的相對連結。")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
