# -*- coding: utf-8 -*-

import os
import shutil
import stat
import subprocess
import tempfile
import unittest


SCRIPT_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'github_pull_request.sh')
)

FAKE_CURL = """#!/usr/bin/env bash
out=""
while [ $# -gt 0 ]; do
    if [ "$1" = "-o" ]; then
        out="$2"
        shift
    fi
    shift
done
cp "$FAKE_DIFF_SOURCE" "$out"
"""

FAKE_PYTHON = """#!/usr/bin/env bash
echo "$@" > "$FAKE_PYTHON_ARGS"
cp "$2" "$FAKE_PYTHON_CAPTURE"
exit "$FAKE_PYTHON_EXIT"
"""


def write_executable(path: str, content: str) -> None:
    with open(path, 'w') as f:
        f.write(content)
    os.chmod(path, os.stat(path).st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


class TestGithubPullRequestScript(unittest.TestCase):

    def setUp(self):
        self.tmp_dir = tempfile.mkdtemp()
        self.workspace = os.path.join(self.tmp_dir, 'workspace')
        self.bin_dir = os.path.join(self.tmp_dir, 'bin')
        os.makedirs(self.workspace)
        os.makedirs(self.bin_dir)

        with open(os.path.join(self.workspace, 'README.md'), 'w') as f:
            f.write('# Public APIs\n')

        write_executable(os.path.join(self.bin_dir, 'curl'), FAKE_CURL)
        write_executable(os.path.join(self.bin_dir, 'python'), FAKE_PYTHON)

        self.diff_source = os.path.join(self.tmp_dir, 'source.diff')
        self.capture = os.path.join(self.tmp_dir, 'captured_additions.txt')
        self.args_capture = os.path.join(self.tmp_dir, 'captured_args.txt')

    def tearDown(self):
        shutil.rmtree(self.tmp_dir, ignore_errors=True)

    def run_script(self, diff: str, python_exit: int = 0) -> subprocess.CompletedProcess:
        with open(self.diff_source, 'w') as f:
            f.write(diff)

        env = dict(os.environ)
        env['PATH'] = self.bin_dir + os.pathsep + env.get('PATH', '')
        env['GITHUB_WORKSPACE'] = self.workspace
        env['FAKE_DIFF_SOURCE'] = self.diff_source
        env['FAKE_PYTHON_CAPTURE'] = self.capture
        env['FAKE_PYTHON_ARGS'] = self.args_capture
        env['FAKE_PYTHON_EXIT'] = str(python_exit)

        return subprocess.run(
            ['bash', SCRIPT_PATH, 'public-apis/public-apis', '123', 'README.md'],
            cwd=self.workspace,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )

    def read_captured_additions(self) -> str:
        with open(self.capture) as f:
            return f.read()

    def test_additions_contain_only_added_lines(self):
        diff = (
            'diff --git a/README.md b/README.md\n'
            '--- a/README.md\n'
            '+++ b/README.md\n'
            '@@ -1,2 +1,3 @@\n'
            ' | Existing | context line |\n'
            '+| New API | https://example.com |\n'
            '-| Removed API | https://removed.example.com |\n'
        )

        result = self.run_script(diff)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(
            self.read_captured_additions(),
            '+| New API | https://example.com |\n'
        )

    def test_additions_exclude_file_header_lines(self):
        diff = (
            '--- a/README.md\n'
            '+++ b/README.md\n'
            '+| New API | https://example.com |\n'
        )

        self.run_script(diff)
        additions = self.read_captured_additions()

        self.assertNotIn('+++', additions)
        self.assertIn('+| New API | https://example.com |', additions)

    def test_additions_exclude_lines_with_plus_in_the_middle(self):
        diff = (
            '+++ b/README.md\n'
            '@@ -10,3 +10,4 @@ ## Category\n'
            ' | C++ API | https://cpp.example.com |\n'
            '-| a+b API | https://ab.example.com |\n'
            '+| Added API | https://added.example.com |\n'
        )

        self.run_script(diff)
        additions = self.read_captured_additions()

        self.assertNotIn('@@', additions)
        self.assertNotIn('C++ API', additions)
        self.assertNotIn('a+b API', additions)
        self.assertEqual(additions, '+| Added API | https://added.example.com |\n')

    def test_multiple_added_lines_are_all_kept(self):
        diff = (
            '+++ b/README.md\n'
            '+| First | https://first.example.com |\n'
            ' | Context | https://context.example.com |\n'
            '+| Second | https://second.example.com |\n'
        )

        self.run_script(diff)

        self.assertEqual(
            self.read_captured_additions(),
            '+| First | https://first.example.com |\n'
            '+| Second | https://second.example.com |\n'
        )

    def test_diff_without_additions_does_not_abort(self):
        diff = (
            '--- a/README.md\n'
            '+++ b/README.md\n'
            '@@ -1,2 +1,1 @@\n'
            '-| Removed API | https://removed.example.com |\n'
        )

        result = self.run_script(diff)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.read_captured_additions(), '')
        self.assertIn('link validation passed on additions!', result.stdout)

    def test_empty_diff_does_not_abort(self):
        result = self.run_script('')

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.read_captured_additions(), '')

    def test_validation_runs_links_script_on_additions_file(self):
        self.run_script('+| New API | https://example.com |\n')

        with open(self.args_capture) as f:
            args = f.read().split()

        self.assertEqual(args, ['scripts/validate/links.py', 'additions.txt'])

    def test_validation_success_reports_passed(self):
        result = self.run_script('+| New API | https://example.com |\n', python_exit=0)

        self.assertEqual(result.returncode, 0)
        self.assertIn('link validation passed on additions!', result.stdout)
        self.assertNotIn('link validation failed on additions!', result.stdout)

    def test_validation_failure_reports_failed_and_exits_with_one(self):
        result = self.run_script('+| New API | https://example.com |\n', python_exit=2)

        self.assertEqual(result.returncode, 1)
        self.assertIn('link validation failed on additions!', result.stdout)
        self.assertNotIn('link validation passed on additions!', result.stdout)

    def test_validation_failure_with_exit_code_one(self):
        result = self.run_script('+| New API | https://example.com |\n', python_exit=1)

        self.assertEqual(result.returncode, 1)
        self.assertIn('link validation failed on additions!', result.stdout)


if __name__ == '__main__':
    unittest.main()
