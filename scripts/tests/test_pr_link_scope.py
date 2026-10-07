import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


class TestPullRequestLinkScope(unittest.TestCase):
    def test_link_validation_receives_only_requested_readme_additions(self):
        # intent: code fixtures cannot become published API links in a README check.
        script = Path(__file__).resolve().parents[1] / 'github_pull_request.sh'
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'README.md').write_text('README\n')
            (root / 'fixture.diff').write_text(
                'diff --git a/scripts/tests/example.py b/scripts/tests/example.py\n'
                '+++ b/scripts/tests/example.py\n'
                '+fixture = "https://fixture.invalid/not-a-public-api"\n'
                'diff --git a/README.md b/README.md\n'
                '+++ b/README.md\n'
                '+Published API link\n'
                '-Removed API link\n'
            )
            tools = root / 'bin'
            tools.mkdir()
            (tools / 'curl').write_text('#!/bin/sh\ncp "$PR_TEST_DIFF" diff.txt\n')
            (tools / 'python').write_text(
                '#!' + sys.executable + '\n'
                'import pathlib, sys\n'
                'assert sys.argv[1:] == ["scripts/validate/links.py", "additions.txt"]\n'
                'assert pathlib.Path("additions.txt").read_text() == "+Published API link\\n"\n'
                'pathlib.Path("validator-ran").write_text("yes")\n'
            )
            for tool in tools.iterdir():
                tool.chmod(0o755)
            env = os.environ.copy()
            env.update({'GITHUB_WORKSPACE': str(root),
                        'PR_TEST_DIFF': str(root / 'fixture.diff'),
                        'PATH': str(tools) + os.pathsep + env['PATH']})
            run = subprocess.run(['bash', str(script), 'owner/repo', '1', 'README.md'],
                                 env=env, text=True, capture_output=True, timeout=10)
            self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
            self.assertEqual((root / 'validator-ran').read_text(), 'yes')
