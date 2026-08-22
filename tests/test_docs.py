from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

import check_links  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]


def test_maintainer_files_exist() -> None:
    required = [
        ROOT / "FORK.md",
        ROOT / "NOTICE.md",
        ROOT / "AGENTS.md",
        ROOT / "CLAUDE.md",
        ROOT / "SECURITY.md",
        ROOT / "REVIEW.md",
        ROOT / "docs" / "UPSTREAM.md",
        ROOT / "docs" / "DECISIONS.md",
        ROOT / "docs" / "DEVELOPMENT.md",
        ROOT / "tools" / "dev_check.ps1",
        ROOT / "tools" / "check_upstream_updates.py",
        ROOT / "requirements-dev.txt",
        ROOT / "README.md",
        ROOT / "LICENSE",
        ROOT / "CONTRIBUTING.md",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
    assert missing == []


def test_readme_stays_the_upstream_catalog() -> None:
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    fork = (ROOT / "FORK.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    assert "不要翻譯或改寫 `README.md`" in agents
    assert "不翻譯、不改寫" in fork
    assert "A collective list of free APIs" in readme or "public APIs" in readme
    assert not (ROOT / "README.en.md").exists()
    assert not (ROOT / "README.zh-Hant.md").exists()


def test_gitignore_covers_generated_reports() -> None:
    gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
    assert "upstream-review-report.md" in gitignore
    assert ".venv" in gitignore


def test_check_links_skips_the_api_catalog() -> None:
    rels = {path.relative_to(ROOT).as_posix() for path in check_links.iter_documents()}
    assert "README.md" not in rels
    assert "scripts/README.md" in rels
    assert "FORK.md" in rels
    assert "docs/UPSTREAM.md" in rels


def test_check_links_rejects_path_outside_repo(tmp_path: Path) -> None:
    doc = tmp_path / "note.md"
    doc.write_text("[here](.)\n", encoding="utf-8")
    problems = check_links.check_document(doc)
    assert any("逃出" in item for item in problems)


def test_non_fork_workflows_have_repo_guard() -> None:
    fork_owned = {"ci.yml", "upstream-check.yml"}
    workflows = ROOT / ".github" / "workflows"
    scanned = 0
    for path in sorted(workflows.glob("*.yml")):
        if path.name in fork_owned:
            continue
        scanned += 1
        text = path.read_text(encoding="utf-8")
        assert "github.repository == 'public-apis/public-apis'" in text, path.name
    assert scanned >= 3


def test_ci_covers_python_314() -> None:
    ci = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    assert "3.14" in ci
    assert "windows" in ci.lower()


def test_fork_ci_does_not_gate_the_catalog_format() -> None:
    ci = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    gate = (ROOT / "tools" / "dev_check.ps1").read_text(encoding="utf-8")

    assert "format.py README.md" not in ci
    assert "format.py" not in gate
    assert "only_duplicate_links" not in ci
    assert "only_duplicate_links" not in gate


def test_maintainer_markdown_links_resolve() -> None:
    failures = 0
    for path in check_links.iter_documents():
        problems = check_links.check_document(path)
        failures += len(problems)
        for problem in problems:
            print(f"{path}: {problem}")
    assert failures == 0
