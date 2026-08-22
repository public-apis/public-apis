from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

import check_upstream_updates as checker  # noqa: E402


def test_baseline_file_is_valid_and_complete() -> None:
    baseline = checker.load_baseline()

    assert baseline["repo"].endswith("public-apis.git")
    assert baseline["branch"] == "master"
    assert len(baseline["reviewed_through"]) == 40
    assert baseline["reviewed_date"]


def test_workflow_is_scheduled_and_fails_on_unreviewed_commits() -> None:
    workflow = (
        Path(__file__).parents[1] / ".github" / "workflows" / "upstream-check.yml"
    ).read_text(encoding="utf-8")

    assert "schedule:" in workflow
    assert "cron:" in workflow
    assert "workflow_dispatch:" in workflow
    assert "tools/check_upstream_updates.py" in workflow
    assert "fetch-depth: 0" in workflow
    assert "exit 1" in workflow


def test_render_markdown_reports_no_new_commits() -> None:
    baseline = {
        "repo": "https://example.invalid/upstream.git",
        "branch": "master",
        "reviewed_through": "a" * 40,
        "reviewed_date": "2026-08-22",
    }

    report = checker.render_markdown(baseline, [])

    assert "No new upstream commits" in report


def test_render_markdown_surfaces_check_failure() -> None:
    baseline = {
        "repo": "https://example.invalid/upstream.git",
        "branch": "master",
        "reviewed_through": "a" * 40,
        "reviewed_date": "2026-08-22",
    }

    report = checker.render_markdown(baseline, [], error="git fetch failed")

    assert "Check failed" in report
    assert "git fetch failed" in report


def test_load_baseline_rejects_missing_file(tmp_path: Path) -> None:
    with pytest.raises(checker.UpstreamCheckError):
        checker.load_baseline(tmp_path / "nope.json")


def test_baseline_matches_decisions_record() -> None:
    decisions = (
        Path(__file__).parents[1] / "docs" / "DECISIONS.md"
    ).read_text(encoding="utf-8")
    baseline = json.loads(
        (Path(__file__).parents[1] / "tools" / "upstream_baseline.json").read_text(
            encoding="utf-8"
        )
    )

    assert baseline["reviewed_date"] in decisions
    assert baseline["reviewed_through"][:7] in (
        Path(__file__).parents[1] / "docs" / "UPSTREAM.md"
    ).read_text(encoding="utf-8")
