"""Report upstream commits that have not yet been reviewed by this fork."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
BASELINE_PATH = REPO_ROOT / "tools" / "upstream_baseline.json"
UPSTREAM_REF_PREFIX = "refs/upstream-check"


class UpstreamCheckError(RuntimeError):
    """Raised when the baseline or upstream Git history cannot be inspected."""


def load_baseline(path: Path = BASELINE_PATH) -> dict:
    if not path.is_file():
        raise UpstreamCheckError(f"missing baseline file: {path}")
    try:
        baseline = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise UpstreamCheckError(f"invalid baseline file: {path}: {exc}") from exc
    required = {"repo", "branch", "reviewed_through", "reviewed_date"}
    missing = sorted(required - baseline.keys())
    if missing:
        raise UpstreamCheckError(f"baseline missing fields: {', '.join(missing)}")
    if len(baseline["reviewed_through"]) != 40:
        raise UpstreamCheckError("reviewed_through must be a full 40-character SHA")
    return baseline


def run_git(args: list[str], repo_dir: Path) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=repo_dir,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if result.returncode != 0:
        raise UpstreamCheckError(
            f"git {' '.join(args)} failed: {result.stderr.strip()}"
        )
    return result.stdout


def fetch_upstream(baseline: dict, repo_dir: Path) -> str:
    branch = baseline["branch"]
    ref = f"{UPSTREAM_REF_PREFIX}/{branch}"
    run_git(
        [
            "fetch",
            "--quiet",
            baseline["repo"],
            f"+refs/heads/{branch}:{ref}",
        ],
        repo_dir,
    )
    return ref


def collect_new_commits(baseline: dict, repo_dir: Path, ref: str) -> list[dict]:
    reviewed = baseline["reviewed_through"]
    raw = run_git(
        [
            "log",
            "--reverse",
            "--date=short",
            "--format=%H%x1f%ad%x1f%s",
            f"{reviewed}..{ref}",
        ],
        repo_dir,
    )
    commits = []
    for line in raw.splitlines():
        if not line.strip():
            continue
        sha, date, subject = line.split("\x1f", 2)
        files = [
            item
            for item in run_git(["show", "--name-only", "--format=", sha], repo_dir).splitlines()
            if item.strip()
        ]
        commits.append(
            {
                "sha": sha,
                "short": sha[:7],
                "date": date,
                "subject": subject,
                "files": files,
            }
        )
    return commits


def render_markdown(
    baseline: dict,
    commits: list[dict],
    error: str | None = None,
) -> str:
    lines = [
        "# Upstream review report",
        "",
        f"- Upstream: `{baseline['repo']}` (`{baseline['branch']}`)",
        f"- Reviewed through: `{baseline['reviewed_through'][:7]}`",
        f"- Last review date: {baseline['reviewed_date']}",
        "",
    ]
    if error:
        lines.extend(["## Check failed", "", f"```text\n{error}\n```", ""])
        return "\n".join(lines)
    if not commits:
        lines.extend(["## Result", "", "No new upstream commits. Nothing to review.", ""])
        return "\n".join(lines)

    lines.extend(
        [
            "## Result",
            "",
            f"{len(commits)} upstream commit(s) require review.",
            "",
            "| Commit | Date | Subject | Files |",
            "| --- | --- | --- | --- |",
        ]
    )
    for commit in commits:
        subject = commit["subject"].replace("|", "\\|")
        files = "<br>".join(item.replace("|", "\\|") for item in commit["files"][:8])
        if len(commit["files"]) > 8:
            files += f"<br>… +{len(commit['files']) - 8} more"
        lines.append(
            f"| `{commit['short']}` | {commit['date']} | {subject} | {files or '(none)'} |"
        )
    lines.extend(
        [
            "",
            "Review each commit, record adopt/skip decisions in `docs/DECISIONS.md`, ",
            "then advance `tools/upstream_baseline.json` only after verification.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="upstream-review-report.md")
    parser.add_argument("--repo-dir", type=Path, default=REPO_ROOT)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return non-zero when new commits require review.",
    )
    args = parser.parse_args()

    baseline: dict
    commits: list[dict] = []
    error: str | None = None
    try:
        baseline = load_baseline()
        ref = fetch_upstream(baseline, args.repo_dir)
        commits = collect_new_commits(baseline, args.repo_dir, ref)
    except UpstreamCheckError as exc:
        error = str(exc)
        baseline = {
            "repo": "unknown",
            "branch": "unknown",
            "reviewed_through": "0" * 40,
            "reviewed_date": "unknown",
        }

    report = render_markdown(baseline, commits, error)
    output = Path(args.output)
    output.write_text(report, encoding="utf-8")
    print(report)

    if error:
        return 2
    if args.strict and commits:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
