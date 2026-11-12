# -*- coding: utf-8 -*-

import os
import shutil
import stat
import subprocess
import tempfile
import textwrap
import unittest


WORKFLOW_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', '..', '.github', 'workflows', 'validate_links.yml'
)


def indentation(line: str) -> int:
    return len(line) - len(line.lstrip(' '))


def load_steps(path: str) -> dict:
    with open(path, encoding='utf-8') as f:
        lines = f.read().splitlines()

    steps = {}
    current_name = None
    step_indent = None

    for line in lines:
        stripped = line.strip()
        if stripped.startswith('- name:') and (step_indent is None or indentation(line) == step_indent):
            step_indent = indentation(line)
            current_name = stripped[len('- name:'):].strip().strip('\'"')
            steps[current_name] = []
            continue
        if current_name is not None:
            if stripped and indentation(line) <= step_indent:
                current_name = None
                continue
            steps[current_name].append(line)

    return steps


def get_key(step_lines: list, key: str) -> str:
    base = min(indentation(line) for line in step_lines if line.strip())
    for line in step_lines:
        if indentation(line) == base and line.strip().startswith(key + ':'):
            return line.strip()[len(key) + 1:].strip()
    return None


def get_with(step_lines: list) -> dict:
    base = min(indentation(line) for line in step_lines if line.strip())
    values = {}
    inside = False
    for line in step_lines:
        if not line.strip():
            continue
        if indentation(line) == base:
            inside = line.strip() == 'with:'
            continue
        if inside and ':' in line:
            k, v = line.strip().split(':', 1)
            values[k.strip()] = v.strip().strip('\'"')
    return values


def get_run_script(step_lines: list) -> str:
    base = min(indentation(line) for line in step_lines if line.strip())
    block = []
    inside = False
    for line in step_lines:
        if indentation(line) == base and line.strip():
            if inside:
                break
            if line.strip().startswith('run:'):
                rest = line.strip()[len('run:'):].strip()
                if rest and rest != '|':
                    return rest
                inside = True
            continue
        if inside:
            block.append(line)
    return textwrap.dedent('\n'.join(block)).strip() + '\n'


class TestValidateLinksWorkflow(unittest.TestCase):

    def setUp(self):
        self.steps = load_steps(WORKFLOW_PATH)
        self.validate_name = 'Validate all links from README.md'
        self.summary_name = 'Add results to job summary'
        self.upload_name = 'Upload results'

    def test_new_steps_exist_in_order(self):
        names = list(self.steps.keys())
        self.assertIn(self.validate_name, names)
        self.assertIn(self.summary_name, names)
        self.assertIn(self.upload_name, names)
        self.assertLess(names.index(self.validate_name), names.index(self.summary_name))
        self.assertLess(names.index(self.summary_name), names.index(self.upload_name))

    def test_validate_step_tees_output_to_file(self):
        script = get_run_script(self.steps[self.validate_name])
        self.assertIn('python scripts/validate/links.py ${FILENAME}', script)
        self.assertIn('| tee broken_links.txt', script)

    def test_validate_step_uses_pipefail(self):
        script = get_run_script(self.steps[self.validate_name])
        self.assertIn('set -o pipefail', script)
        self.assertLess(script.index('set -o pipefail'), script.index('tee broken_links.txt'))

    def test_summary_step_always_runs(self):
        self.assertEqual(get_key(self.steps[self.summary_name], 'if'), 'always()')

    def test_upload_step_always_runs(self):
        self.assertEqual(get_key(self.steps[self.upload_name], 'if'), 'always()')

    def test_upload_step_uses_upload_artifact_v4(self):
        self.assertEqual(get_key(self.steps[self.upload_name], 'uses'), 'actions/upload-artifact@v4')

    def test_upload_step_configuration(self):
        config = get_with(self.steps[self.upload_name])
        self.assertEqual(config.get('name'), 'broken-links')
        self.assertEqual(config.get('path'), 'broken_links.txt')
        self.assertEqual(config.get('if-no-files-found'), 'ignore')
        self.assertEqual(config.get('retention-days'), '90')


@unittest.skipIf(shutil.which('bash') is None, 'bash is required')
class TestValidateLinksWorkflowScripts(unittest.TestCase):

    def setUp(self):
        self.steps = load_steps(WORKFLOW_PATH)
        self.workdir = tempfile.mkdtemp()
        self.bindir = os.path.join(self.workdir, 'bin')
        os.mkdir(self.bindir)
        self.summary_file = os.path.join(self.workdir, 'summary.md')

    def tearDown(self):
        shutil.rmtree(self.workdir)

    def make_fake_python(self, output: str, exit_code: int):
        path = os.path.join(self.bindir, 'python')
        with open(path, 'w', encoding='utf-8') as f:
            f.write('#!/usr/bin/env bash\n')
            f.write('printf %s "{}"\n'.format(output))
            f.write('exit {}\n'.format(exit_code))
        os.chmod(path, os.stat(path).st_mode | stat.S_IEXEC)

    def run_step(self, name: str) -> subprocess.CompletedProcess:
        script = get_run_script(self.steps[name])
        env = dict(os.environ)
        env['PATH'] = self.bindir + os.pathsep + env.get('PATH', '')
        env['FILENAME'] = 'README.md'
        env['GITHUB_STEP_SUMMARY'] = self.summary_file
        return subprocess.run(
            ['bash', '-e', '-c', script],
            cwd=self.workdir, env=env,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            universal_newlines=True,
        )

    def read(self, filename: str) -> str:
        with open(os.path.join(self.workdir, filename), encoding='utf-8') as f:
            return f.read()

    def test_validate_step_fails_when_links_are_broken(self):
        self.make_fake_python('ERR:CLT: 404 : https://broken.example.com\n', 1)
        result = self.run_step('Validate all links from README.md')
        self.assertNotEqual(result.returncode, 0)

    def test_validate_step_saves_output_when_links_are_broken(self):
        self.make_fake_python('ERR:CLT: 404 : https://broken.example.com\n', 1)
        result = self.run_step('Validate all links from README.md')
        self.assertIn('https://broken.example.com', self.read('broken_links.txt'))
        self.assertIn('https://broken.example.com', result.stdout)

    def test_validate_step_succeeds_when_all_links_work(self):
        self.make_fake_python('Checking links...\n', 0)
        result = self.run_step('Validate all links from README.md')
        self.assertEqual(result.returncode, 0)
        self.assertEqual(self.read('broken_links.txt'), 'Checking links...\n')

    def test_summary_step_writes_results_in_code_block(self):
        with open(os.path.join(self.workdir, 'broken_links.txt'), 'w', encoding='utf-8') as f:
            f.write('ERR:CLT: 404 : https://broken.example.com\n')
        result = self.run_step('Add results to job summary')
        self.assertEqual(result.returncode, 0)
        with open(self.summary_file, encoding='utf-8') as f:
            summary = f.read()
        self.assertEqual(
            summary,
            '## Link validation results\n'
            '```\n'
            'ERR:CLT: 404 : https://broken.example.com\n'
            '```\n'
        )

    def test_summary_step_appends_to_existing_summary(self):
        with open(self.summary_file, 'w', encoding='utf-8') as f:
            f.write('previous\n')
        with open(os.path.join(self.workdir, 'broken_links.txt'), 'w', encoding='utf-8') as f:
            f.write('result\n')
        self.run_step('Add results to job summary')
        with open(self.summary_file, encoding='utf-8') as f:
            summary = f.read()
        self.assertTrue(summary.startswith('previous\n## Link validation results\n'))

    def test_summary_step_skips_when_no_results_file(self):
        result = self.run_step('Add results to job summary')
        self.assertEqual(result.returncode, 0)
        self.assertFalse(os.path.exists(self.summary_file))


if __name__ == '__main__':
    unittest.main()
