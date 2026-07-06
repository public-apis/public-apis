# -*- coding: utf-8 -*-

"""Unit tests for scripts/validate/format.py (current 5-column schema)."""

import unittest

from validate.format import (
    anchorize,
    check_description_column,
    check_duplicate_functions,
    check_file,
    check_function_column,
    check_header_column,
    check_index_sync,
    check_mtsafe_column,
    check_mtsafe_consistency,
    check_standard_column,
    error_message,
    is_table_header,
    is_table_separator,
    parse_line,
)

from tests.test_helpers import (
    DUP_FUNCTION_README,
    INDEX_MISMATCH_README,
    MTSAFE_MISMATCH_README,
    VALID_README,
)


def _to_lines(text: str) -> list[str]:
    return [line.rstrip() for line in text.splitlines()]


class TestErrorMessage(unittest.TestCase):
    def test_format_and_line_numbers(self):
        self.assertEqual(error_message(0, 'boom'), 'Line    1: boom')
        self.assertEqual(error_message(9, 'boom'), 'Line   10: boom')
        self.assertEqual(error_message(99, 'boom'), 'Line  100: boom')
        self.assertEqual(error_message(999, 'boom'), 'Line 1000: boom')


class TestAnchorize(unittest.TestCase):
    def test_basic_slug(self):
        self.assertEqual(anchorize('Standard I/O (stdio.h)'), 'standard-io-stdioh')

    def test_ampersand_becomes_double_hyphen(self):
        self.assertEqual(
            anchorize('Character & String (string.h, ctype.h)'),
            'character--string-stringh-ctypeh',
        )

    def test_raw_entity_diverges_from_decoded_anchor(self):
        # GitHub slugifies the *raw* source, so '&amp;' yields 'amp' in the slug.
        self.assertEqual(
            anchorize('Environment &amp; System Info (unistd.h, sys/utsname.h)'),
            'environment-amp-system-info-unistdh-sysutsnameh',
        )
        # A literal '&' (the corrected form) matches the Index anchor.
        self.assertEqual(
            anchorize('Environment & System Info (unistd.h, sys/utsname.h)'),
            'environment--system-info-unistdh-sysutsnameh',
        )


class TestColumnChecks(unittest.TestCase):
    def test_function_column(self):
        self.assertIsNone(check_function_column(
            '[fopen](https://man7.org/linux/man-pages/man3/fopen.3.html)'))
        self.assertIsNotNone(check_function_column('fopen'))
        self.assertIsNotNone(check_function_column(
            '[fopen](https://example.com/not-man7)'))

    def test_header_column(self):
        self.assertIsNone(check_header_column('`<stdio.h>`'))
        self.assertIsNotNone(check_header_column('stdio.h'))
        self.assertIsNotNone(check_header_column('`<Foo.h>`'))

    def test_description_column(self):
        self.assertIsNone(check_description_column('Open a file'))
        self.assertIsNotNone(check_description_column(''))
        self.assertIsNotNone(check_description_column('open a file'))
        self.assertIsNotNone(check_description_column('x' * 201))

    def test_standard_column(self):
        self.assertIsNone(check_standard_column('POSIX.1-2001, C89'))
        self.assertIsNone(check_standard_column('C99'))
        self.assertIsNone(check_standard_column('GNU'))
        self.assertIsNotNone(check_standard_column('foo bar!'))

    def test_mtsafe_column(self):
        self.assertIsNone(check_mtsafe_column('Yes'))
        self.assertIsNone(check_mtsafe_column('No'))
        self.assertIsNone(check_mtsafe_column('No (race:strtok)'))
        self.assertIsNotNone(check_mtsafe_column('yes'))
        self.assertIsNotNone(check_mtsafe_column('Maybe'))
        self.assertIsNotNone(check_mtsafe_column('No (race'))


class TestParseLine(unittest.TestCase):
    def test_valid_row(self):
        row = ('| [fopen](https://man7.org/linux/man-pages/man3/fopen.3.html) '
               '| `<stdio.h>` | Open a file | POSIX.1-2001, C89 | Yes |')
        cols = parse_line(row)
        self.assertEqual(cols, [
            '[fopen](https://man7.org/linux/man-pages/man3/fopen.3.html)',
            '`<stdio.h>`', 'Open a file', 'POSIX.1-2001, C89', 'Yes',
        ])

    def test_non_row_returns_none(self):
        self.assertIsNone(parse_line('## Module'))
        self.assertIsNone(parse_line('| --- | --- | --- | --- | --- |'))
        self.assertIsNone(parse_line('| only | four | cols |'))

    def test_table_header_and_separator(self):
        self.assertTrue(is_table_header(
            '| Function | Header | Description | Standard | MT-Safe |'))
        self.assertFalse(is_table_header('| foo | bar |'))
        self.assertTrue(is_table_separator('| --- | --- | --- | --- | --- |'))
        self.assertFalse(is_table_separator('| --- |'))


class TestCheckDuplicateFunctions(unittest.TestCase):
    def test_no_duplicates(self):
        errors, warnings = check_duplicate_functions(_to_lines(VALID_README))
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_duplicate_in_same_module_is_error(self):
        errors, warnings = check_duplicate_functions(_to_lines(DUP_FUNCTION_README))
        self.assertEqual(len(errors), 1)
        self.assertIn('Duplicate function "sin"', errors[0])
        self.assertEqual(warnings, [])

    def test_cross_module_same_name_is_allowed(self):
        # strerror appears in two modules in MTSAFE_MISMATCH_README -> no error.
        errors, _ = check_duplicate_functions(_to_lines(MTSAFE_MISMATCH_README))
        self.assertEqual(errors, [])


class TestCheckIndexSync(unittest.TestCase):
    def test_valid_readme_in_sync(self):
        self.assertEqual(check_index_sync(_to_lines(VALID_README)), [])

    def test_entity_heading_is_caught(self):
        errors = check_index_sync(_to_lines(INDEX_MISMATCH_README))
        self.assertTrue(errors)
        # The broken '&amp;' heading yields the '...-amp-system-info-...' slug,
        # which diverges from the Index anchor and must be reported.
        self.assertTrue(
            any('environment-amp-system-info' in e for e in errors),
            msg=f'expected the broken &amp; slug to be reported, got: {errors}',
        )

    def test_fixed_heading_passes(self):
        fixed = INDEX_MISMATCH_README.replace('&amp;', '&')
        self.assertEqual(check_index_sync(_to_lines(fixed)), [])


class TestCheckMtsafeConsistency(unittest.TestCase):
    def test_consistent_readme_has_no_warning(self):
        self.assertEqual(check_mtsafe_consistency(_to_lines(VALID_README)), [])

    def test_conflicting_values_warn(self):
        warnings = check_mtsafe_consistency(_to_lines(MTSAFE_MISMATCH_README))
        self.assertEqual(len(warnings), 1)
        self.assertIn('MT-Safe inconsistent for "strerror"', warnings[0])


class TestCheckFile(unittest.TestCase):
    def _write_temp(self, text: str) -> str:
        import tempfile
        import os
        tf = tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8')
        tf.write(text)
        tf.close()
        self.addCleanup(os.unlink, tf.name)
        return tf.name

    def test_valid_readme_has_no_errors(self):
        path = self._write_temp(VALID_README)
        self.assertEqual(check_file(path), [])

    def test_duplicate_propagates_to_check_file(self):
        path = self._write_temp(DUP_FUNCTION_README)
        errors = check_file(path)
        self.assertTrue(any('Duplicate function' in e for e in errors))

    def test_index_mismatch_propagates_to_check_file(self):
        path = self._write_temp(INDEX_MISMATCH_README)
        errors = check_file(path)
        self.assertTrue(any('Index' in e for e in errors))


if __name__ == '__main__':
    unittest.main()
