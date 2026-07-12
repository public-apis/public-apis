# -*- coding: utf-8 -*-

import unittest

from validate.format import (
    error_message,
    warning_message,
    check_function_column,
    check_header_column,
    check_description_column,
    check_standard_column,
    check_mtsafe_column,
    parse_line,
    is_table_header,
    is_table_separator,
    check_alphabetical_order,
    check_file,
)


class TestValidateFormat(unittest.TestCase):

    def test_error_message_format(self):
        self.assertEqual(error_message(0, 'boom'), 'Line    1: boom')
        self.assertEqual(error_message(99, 'boom'), 'Line  100: boom')

    def test_warning_message_format(self):
        self.assertEqual(warning_message(0, 'soft'), 'Line    1: [warn] soft')

    # --- column checks -------------------------------------------------

    def test_check_function_column(self):
        self.assertIsNone(check_function_column('[fopen](https://man7.org/linux/man-pages/man3/fopen.3.html)'))
        self.assertIsNotNone(check_function_column('fopen'))
        self.assertIsNotNone(check_function_column('[fopen](https://example.com/x)'))

    def test_check_header_column(self):
        self.assertIsNone(check_header_column('`<stdio.h>`'))
        self.assertIsNotNone(check_header_column('stdio.h'))
        self.assertIsNotNone(check_header_column('`<stdio>`'))

    def test_check_description_column(self):
        self.assertIsNone(check_description_column('Open a file'))
        self.assertIsNotNone(check_description_column(''))              # empty
        self.assertIsNotNone(check_description_column('open a file'))  # lowercase
        self.assertIsNotNone(check_description_column('x' * 201))       # too long

    def test_check_standard_column(self):
        self.assertIsNone(check_standard_column('C89'))
        self.assertIsNone(check_standard_column('POSIX.1-2001, C89'))
        self.assertIsNone(check_standard_column('BSD (foo)'))
        self.assertIsNotNone(check_standard_column('??'))

    def test_check_mtsafe_column(self):
        self.assertIsNone(check_mtsafe_column('Yes'))
        self.assertIsNone(check_mtsafe_column('No (race:tmpnam)'))
        self.assertIsNotNone(check_mtsafe_column('Maybe'))
        self.assertIsNotNone(check_mtsafe_column('yes'))

    # --- parse / header helpers ----------------------------------------

    def test_parse_line(self):
        row = '| [fopen](https://man7.org/linux/man-pages/man3/fopen.3.html) | `<stdio.h>` | Open a file | C89 | Yes |'
        self.assertEqual(
            parse_line(row),
            ['[fopen](https://man7.org/linux/man-pages/man3/fopen.3.html)',
             '`<stdio.h>`', 'Open a file', 'C89', 'Yes'],
        )
        self.assertIsNone(parse_line('not a table row'))
        self.assertIsNone(parse_line('| --- | --- | --- | --- | --- |'))

    def test_is_table_header_and_separator(self):
        self.assertTrue(is_table_header('| Function | Header | Description | Standard | MT-Safe |'))
        self.assertFalse(is_table_header('| fopen | ... |'))
        self.assertTrue(is_table_separator('| --- | --- | --- | --- | --- |'))
        self.assertFalse(is_table_separator('| --- | --- |'))

    # --- alphabetical order (migrated upstream discipline) -------------

    def test_check_alphabetical_order_sorted(self):
        self.assertEqual(check_alphabetical_order(['fclose', 'fdopen', 'fileno', 'fopen', 'freopen']), [])

    def test_check_alphabetical_order_unsorted(self):
        self.assertEqual(check_alphabetical_order(['fopen', 'freopen', 'fdopen', 'fclose', 'fileno']), [2, 3])

    # --- full file check ------------------------------------------------

    def test_check_file_clean(self):
        clean = [
            '### Stream Open/Close',
            '| Function | Header | Description | Standard | MT-Safe |',
            '| --- | --- | --- | --- | --- |',
            '| [fclose](https://man7.org/linux/man-pages/man3/fclose.3.html) | `<stdio.h>` | Close a stream | POSIX.1-2001, C89 | Yes |',
            '| [fdopen](https://man7.org/linux/man-pages/man3/fdopen.3.html) | `<stdio.h>` | Associate a stream with an fd | POSIX.1-2001, POSIX.1-2008 | Yes |',
            '| [fileno](https://man7.org/linux/man-pages/man3/fileno.3.html) | `<stdio.h>` | Return the fd of a stream | POSIX.1-2001, POSIX.1-2008 | Yes |',
        ]
        errors, warnings = check_file_from_lines(clean)
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_check_file_column_errors(self):
        bad = [
            '### Bad',
            '| Function | Header | Description | Standard | MT-Safe |',
            '| --- | --- | --- | --- | --- |',
            '| fopen | `<stdio.h>` | Open a file | C89 | Yes |',   # function not a link
        ]
        errors, _ = check_file_from_lines(bad)
        self.assertEqual(len(errors), 1)

    def test_check_file_alphabetical_warning(self):
        unsorted = [
            '### Stream Open/Close',
            '| Function | Header | Description | Standard | MT-Safe |',
            '| --- | --- | --- | --- | --- |',
            '| [fopen](https://man7.org/linux/man-pages/man3/fopen.3.html) | `<stdio.h>` | Open a file | POSIX.1-2001, C89 | Yes |',
            '| [fdopen](https://man7.org/linux/man-pages/man3/fdopen.3.html) | `<stdio.h>` | Associate a stream with an fd | POSIX.1-2001, POSIX.1-2008 | Yes |',
        ]
        errors, warnings = check_file_from_lines(unsorted)
        self.assertEqual(errors, [])
        self.assertEqual(len(warnings), 1)
        self.assertIn('not in alphabetical order', warnings[0])

    def test_check_file_obsolete_warning(self):
        obsolete = [
            '### Deprecated',
            '| Function | Header | Description | Standard | MT-Safe |',
            '| --- | --- | --- | --- | --- |',
            '| [gets](https://man7.org/linux/man-pages/man3/gets.3.html) | `<stdio.h>` | Read a line from stdin | POSIX.1-2001 (removed in C11) | Yes |',
        ]
        errors, warnings = check_file_from_lines(obsolete)
        self.assertEqual(errors, [])
        self.assertEqual(len(warnings), 1)
        self.assertIn('deprecated', warnings[0])

    def test_check_file_short_desc_warning(self):
        short = [
            '### Short',
            '| Function | Header | Description | Standard | MT-Safe |',
            '| --- | --- | --- | --- | --- |',
            '| [foo](https://man7.org/linux/man-pages/man3/foo.3.html) | `<foo.h>` | Bar | C89 | Yes |',
        ]
        errors, warnings = check_file_from_lines(short)
        self.assertEqual(errors, [])
        self.assertEqual(len(warnings), 1)
        self.assertIn('very short', warnings[0])


def check_file_from_lines(lines):
    """Helper: write lines to a temp file and run check_file."""
    import tempfile
    import os
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as tf:
        tf.write('\n'.join(lines) + '\n')
        path = tf.name
    try:
        return check_file(path)
    finally:
        os.unlink(path)


if __name__ == '__main__':
    unittest.main()
