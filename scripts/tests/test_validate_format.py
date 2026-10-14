# -*- coding: utf-8 -*-

import unittest

from validate.format import error_message
from validate.format import get_categories_content
from validate.format import check_alphabetical_order
from validate.format import check_title
from validate.format import check_description, max_description_length
from validate.format import check_auth, auth_keys
from validate.format import check_https, https_keys
from validate.format import check_cors, cors_keys
from validate.format import check_entry
from validate.format import check_file_format, min_entries_per_category, num_segments
from validate.format import check_mcp_entry, num_segments
from validate.format import transport_keys
from validate.format import get_header_table_kind
from validate.format import is_separator_row
from validate.format import rest_table, mcp_table, sponsored_table


class TestValidadeFormat(unittest.TestCase):
    



    def test_mcp_order_is_checked_without_becoming_a_rest_category(self):
        # intent: MCP ordering remains checked independently of REST category counts.
        lines = ['## MCP Servers', '| Name | Description | Auth | Transport | Install |',
                 '| [Zed](https://example.com) | Desc | No | `HTTP` | – |',
                 '| [Alpha](https://example.com) | Desc | No | `HTTP` | – |']
        self.assertTrue(check_alphabetical_order(lines))
        self.assertEqual(get_categories_content(lines)[0], {})
        lines[-2:] = list(reversed(lines[-2:]))
        self.assertEqual(check_alphabetical_order(lines), [])

    def test_documented_six_column_rest_table_remains_valid(self):
        # intent: the optional Postman column is part of the published REST format.
        lines = ['* [A](#a)', '### A',
                 '| API | Description | Auth | HTTPS | CORS | Call this API |',
                 '|:---|:---|:---|:---|:---|:---|']
        lines += ['| [A{}](https://example.com/{}) | Desc | No | Yes | Yes | [Run](https://postman.com) |'.format(i, i) for i in range(3)]
        self.assertEqual(check_file_format(lines), [])

    def test_indexed_categories_cannot_switch_to_sponsored_or_mcp_tables(self):
        # intent: changing a REST header cannot hide invalid HTTPS/CORS values.
        for header in ('| API | Description | Call this API |',
                       '| Name | Description | Auth | Transport | Install |'):
            lines = ['* [A](#a)', '### A', header,
                     '| [AA](https://example.com) | Desc | Bogus | Bad | Bad |']
            with self.subTest(header=header):
                errors = check_file_format(lines)
                self.assertTrue(any('HTTPS option' in error for error in errors))
                self.assertTrue(any('CORS option' in error for error in errors))

    def test_empty_indexed_category_still_requires_entries(self):
        # intent: an empty category cannot evade the minimum-entry guard.
        lines = ['* [A](#a)', '* [B](#b)', '### A', '### B',
                 '| [BB](https://example.com) | Desc | No | Yes | Yes |',
                 '| [BC](https://example.com) | Desc | No | Yes | Yes |',
                 '| [BD](https://example.com) | Desc | No | Yes | Yes |']
        self.assertTrue(any('minimum' in error for error in check_file_format(lines)))

    def test_error_message_return_and_return_type(self):
        line_num_unity = 1
        line_num_ten = 10
        line_num_hundred = 100
        line_num_thousand = 1000

        msg = 'This is a unit test'

        err_msg_unity = error_message(line_num_unity, msg)
        err_msg_ten = error_message(line_num_ten, msg)
        err_msg_hundred = error_message(line_num_hundred, msg)
        err_msg_thousand = error_message(line_num_thousand, msg)

        self.assertIsInstance(err_msg_unity, str)
        self.assertIsInstance(err_msg_ten, str)
        self.assertIsInstance(err_msg_hundred, str)
        self.assertIsInstance(err_msg_thousand, str)

        self.assertEqual(err_msg_unity, '(L002) This is a unit test')
        self.assertEqual(err_msg_ten, '(L011) This is a unit test')
        self.assertEqual(err_msg_hundred, '(L101) This is a unit test')
        self.assertEqual(err_msg_thousand, '(L1001) This is a unit test')

    def test_if_get_categories_content_return_correct_data_of_categories(self):
        fake_contents = [
            '### A',
            'API | Description | Auth | HTTPS | CORS |',
            '|---|---|---|---|---|',
            '| [AA](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '| [AB](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '',
            '### B',
            'API | Description | Auth | HTTPS | CORS |',
            '|---|---|---|---|---|',
            '| [BA](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '| [BB](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |'
        ]

        result = get_categories_content(fake_contents)
        self.assertIsInstance(result, tuple)

        categories, category_line_num = result
        self.assertIsInstance(categories, dict)
        self.assertIsInstance(category_line_num, dict)

        expected_result = ({'A': ['AA', 'AB'], 'B': ['BA', 'BB']}, {'A': 0, 'B': 6})

        for res, ex_res in zip(result, expected_result):

            with self.subTest():
                self.assertEqual(res, ex_res)

    def test_if_check_alphabetical_order_return_correct_msg_error(self):
        correct_lines = [
            '### A',
            'API | Description | Auth | HTTPS | CORS |',
            '|---|---|---|---|---|',
            '| [AA](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '| [AB](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '',
            '### B',
            'API | Description | Auth | HTTPS | CORS |',
            '|---|---|---|---|---|',
            '| [BA](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '| [BB](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |'
        ]

        incorrect_lines = [
            '### A',
            'API | Description | Auth | HTTPS | CORS |',
            '|---|---|---|---|---|',
            '| [AB](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '| [AA](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '',
            '### B',
            'API | Description | Auth | HTTPS | CORS |',
            '|---|---|---|---|---|',
            '| [BB](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '| [BA](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |'
        ]


        err_msgs_1 = check_alphabetical_order(correct_lines)
        err_msgs_2 = check_alphabetical_order(incorrect_lines)

        self.assertIsInstance(err_msgs_1, list)
        self.assertIsInstance(err_msgs_2, list)

        self.assertEqual(len(err_msgs_1), 0)
        self.assertEqual(len(err_msgs_2), 2)

        expected_err_msgs = [
            '(L001) A category is not alphabetical order',
            '(L007) B category is not alphabetical order'
        ]

        for err_msg, ex_err_msg in zip(err_msgs_2, expected_err_msgs):

            with self.subTest():
                self.assertEqual(err_msg, ex_err_msg)
    
    def test_check_title_with_correct_title(self):
        raw_title = '[A](https://www.ex.com)'

        err_msgs = check_title(0, raw_title)

        self.assertIsInstance(err_msgs, list)
        self.assertEqual(len(err_msgs), 0)
        self.assertEqual(err_msgs, [])

    def test_check_title_with_markdown_syntax_incorrect(self):
        raw_title = '[A(https://www.ex.com)'

        err_msgs = check_title(0, raw_title)

        self.assertIsInstance(err_msgs, list)
        self.assertEqual(len(err_msgs), 1)
        
        err_msg = err_msgs[0]
        expected_err_msg = '(L001) Title syntax should be "[TITLE](LINK)"'

        self.assertEqual(err_msg, expected_err_msg)

    def test_check_title_with_api_at_the_end_of_the_title(self):
        raw_title = '[A API](https://www.ex.com)'

        err_msgs = check_title(0, raw_title)
        
        self.assertIsInstance(err_msgs, list)
        self.assertEqual(len(err_msgs), 1)
        
        err_msg = err_msgs[0]
        expected_err_msg = '(L001) Title should not end with "... API". Every entry is an API here!'

        self.assertEqual(err_msg, expected_err_msg)

    def test_check_description_with_correct_description(self):
        desc = 'This is a fake description'

        err_msgs = check_description(0, desc)

        self.assertIsInstance(err_msgs, list)
        self.assertEqual(len(err_msgs), 0)
        self.assertEqual(err_msgs, [])
    
    def test_check_description_with_first_char_is_not_capitalized(self):
        desc = 'this is a fake description'

        err_msgs = check_description(0, desc)

        self.assertIsInstance(err_msgs, list)
        self.assertEqual(len(err_msgs), 1)
        
        err_msg = err_msgs[0]
        expected_err_msg = '(L001) first character of description is not capitalized'

        self.assertIsInstance(err_msg, str)
        self.assertEqual(err_msg, expected_err_msg)
    
    def test_check_description_with_punctuation_in_the_end(self):
        base_desc = 'This is a fake description'
        punctuation = r"""!"#$%&'*+,-./:;<=>?@[\]^_`{|}~"""
        desc_with_punc = [base_desc + punc for punc in punctuation]
        
        for desc in desc_with_punc:

            with self.subTest():
                err_msgs = check_description(0, desc)

                self.assertIsInstance(err_msgs, list)
                self.assertEqual(len(err_msgs), 1)
        
                err_msg = err_msgs[0]
                expected_err_msg = f'(L001) description should not end with {desc[-1]}'

                self.assertIsInstance(err_msg, str)
                self.assertEqual(err_msg, expected_err_msg)

    def test_check_description_that_exceeds_the_character_limit(self):
        long_desc = 'Desc' * max_description_length
        long_desc_length = len(long_desc)

        err_msgs = check_description(0, long_desc)

        self.assertIsInstance(err_msgs, list)
        self.assertEqual(len(err_msgs), 1)

        err_msg = err_msgs[0]
        expected_err_msg = f'(L001) description should not exceed {max_description_length} characters (currently {long_desc_length})'

        self.assertIsInstance(err_msg, str)
        self.assertEqual(err_msg, expected_err_msg)

    def test_check_auth_with_valid_auth(self):
        auth_valid = [f'`{auth}`' for auth in auth_keys if auth != 'No']
        auth_valid.append('No')

        for auth in auth_valid:
            with self.subTest():
                err_msgs = check_auth(0, auth)
                self.assertIsInstance(err_msgs, list)
                self.assertEqual(len(err_msgs), 0)
                self.assertEqual(err_msgs, [])

    def test_check_auth_without_backtick(self):
        auth_without_backtick = [auth for auth in auth_keys if auth != 'No']

        for auth in auth_without_backtick:
            with self.subTest():
                err_msgs = check_auth(0, auth)
                self.assertIsInstance(err_msgs, list)
                self.assertEqual(len(err_msgs), 1)

                err_msg = err_msgs[0]
                expected_err_msg = '(L001) auth value is not enclosed with `backticks`'

                self.assertIsInstance(err_msg, str)
                self.assertEqual(err_msg, expected_err_msg)

    def test_check_auth_with_invalid_auth(self):
        auth_invalid_without_backtick = ['Yes', 'yes', 'no', 'random', 'Unknown']
        auth_invalid_with_backtick = ['`Yes`', '`yes`', '`no`', '`random`', '`Unknown`']

        for auth in auth_invalid_without_backtick:
            with self.subTest():
                err_msgs = check_auth(0, auth)
                self.assertIsInstance(err_msgs, list)
                self.assertEqual(len(err_msgs), 2)

                err_msg_1 = err_msgs[0]
                err_msg_2 = err_msgs[1]

                expected_err_msg_1 = f'(L001) auth value is not enclosed with `backticks`'
                expected_err_msg_2 = f'(L001) {auth} is not a valid Auth option'

                self.assertIsInstance(err_msg_1, str)
                self.assertIsInstance(err_msg_2, str)
                self.assertEqual(err_msg_1, expected_err_msg_1)
                self.assertEqual(err_msg_2, expected_err_msg_2)

        for auth in auth_invalid_with_backtick:
            with self.subTest():
                err_msgs = check_auth(0, auth)
                self.assertIsInstance(err_msgs, list)
                self.assertEqual(len(err_msgs), 1)

                err_msg = err_msgs[0]
                expected_err_msg = f'(L001) {auth} is not a valid Auth option'

                self.assertIsInstance(err_msg, str)
                self.assertEqual(err_msg, expected_err_msg)

    def test_check_https_with_valid_https(self):
        for https in https_keys:
            with self.subTest():
                err_msgs = check_https(0, https)
                self.assertIsInstance(err_msgs, list)
                self.assertEqual(len(err_msgs), 0)
                self.assertEqual(err_msgs, [])

    def test_check_https_with_invalid_https(self):
        invalid_https_keys = ['yes', 'no', 'Unknown', 'https', 'http']

        for https in invalid_https_keys:
            with self.subTest():
                err_msgs = check_https(0, https)
                self.assertIsInstance(err_msgs, list)
                self.assertEqual(len(err_msgs), 1)

                err_msg = err_msgs[0]
                expected_err_msg = f'(L001) {https} is not a valid HTTPS option'

                self.assertIsInstance(err_msg, str)
                self.assertEqual(err_msg, expected_err_msg)

    def test_check_cors_with_valid_cors(self):
        for cors in cors_keys:
            with self.subTest():
                err_msgs = check_cors(0, cors)
                self.assertIsInstance(err_msgs, list)
                self.assertEqual(len(err_msgs), 0)
                self.assertEqual(err_msgs, [])

    def test_check_cors_with_invalid_cors(self):
        invalid_cors_keys = ['yes', 'no', 'unknown', 'cors']

        for cors in invalid_cors_keys:
            with self.subTest():
                err_msgs = check_cors(0, cors)
                self.assertIsInstance(err_msgs, list)
                self.assertEqual(len(err_msgs), 1)

                err_msg = err_msgs[0]
                expected_err_msg = f'(L001) {cors} is not a valid CORS option'

                self.assertIsInstance(err_msg, str)
                self.assertEqual(err_msg, expected_err_msg)

    def test_check_entry_with_correct_segments(self):
        correct_segments = ['[A](https://www.ex.com)', 'Desc', '`apiKey`', 'Yes', 'Yes']

        err_msgs = check_entry(0, correct_segments)
        
        self.assertIsInstance(err_msgs, list)
        self.assertEqual(len(err_msgs), 0)
        self.assertEqual(err_msgs, [])

    def test_check_entry_with_incorrect_segments(self):
        incorrect_segments = ['[A API](https://www.ex.com)', 'desc.', 'yes', 'yes', 'yes']

        err_msgs = check_entry(0, incorrect_segments)
        expected_err_msgs = [
            '(L001) Title should not end with "... API". Every entry is an API here!',
            '(L001) first character of description is not capitalized',
            '(L001) description should not end with .',
            '(L001) auth value is not enclosed with `backticks`',
            '(L001) yes is not a valid Auth option',
            '(L001) yes is not a valid HTTPS option',
            '(L001) yes is not a valid CORS option'
        ]

        self.assertIsInstance(err_msgs, list)
        self.assertEqual(len(err_msgs), 7)
        for err_msg in err_msgs:
            with self.subTest():
                self.assertIsInstance(err_msg, str)
        self.assertEqual(err_msgs, expected_err_msgs)

    def test_check_file_format_with_correct_format(self):
        correct_format = [
            '## Index',
            '* [A](#a)',
            '* [B](#b)',
            '',
            '### A',
            'API | Description | Auth | HTTPS | CORS |',
            '|---|---|---|---|---|',
            '| [AA](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '| [AB](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '| [AC](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '',
            '### B',
            'API | Description | Auth | HTTPS | CORS |',
            '|---|---|---|---|---|',
            '| [BA](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '| [BB](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '| [BC](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |'
        ]

        err_msgs = check_file_format(lines=correct_format)

        self.assertIsInstance(err_msgs, list)
        self.assertEqual(len(err_msgs), 0)
        self.assertEqual(err_msgs, [])

    def test_check_file_format_with_category_header_not_added_to_index(self):
        incorrect_format = [
            '## Index',
            '',
            '### A',
            'API | Description | Auth | HTTPS | CORS |',
            '|---|---|---|---|---|',
            '| [AA](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '| [AB](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '| [AC](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
        ]

        err_msgs = check_file_format(lines=incorrect_format)
        expected_err_msg = '(L003) category header (A) not added to Index section'

        self.assertIsInstance(err_msgs, list)
        self.assertEqual(len(err_msgs), 1)
        err_msg = err_msgs[0]
        self.assertEqual(err_msg, expected_err_msg)

    def test_check_file_format_with_category_without_min_entries(self):
        incorrect_format = [
            '## Index',
            '* [A](#a)',
            '* [B](#b)',
            '',
            '### A',
            'API | Description | Auth | HTTPS | CORS |',
            '|---|---|---|---|---|',
            '| [AA](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '',
            '### B',
            'API | Description | Auth | HTTPS | CORS |',
            '|---|---|---|---|---|',
            '| [BA](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '| [BB](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '| [BC](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |'
        ]

        category_with_err = 'A'
        num_in_category = 1

        err_msgs = check_file_format(lines=incorrect_format)
        expected_err_msg = f'(L005) {category_with_err} category does not have the minimum {min_entries_per_category} entries (only has {num_in_category})'

        self.assertIsInstance(err_msgs, list)
        self.assertEqual(len(err_msgs), 1)
        err_msg = err_msgs[0]
        self.assertEqual(err_msg, expected_err_msg)

    def test_check_file_format_entry_without_all_necessary_columns(self):
        incorrect_format = [
            '## Index',
            '* [A](#a)',
            '',
            '### A',
            'API | Description | Auth | HTTPS | CORS |',
            '|---|---|---|---|---|',
            '| [AA](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '| [AB](https://www.ex.com) | Desc | `apiKey` |',  # missing https and cors
            '| [AC](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
        ]

        current_segments_num = 3

        err_msgs = check_file_format(lines=incorrect_format)
        expected_err_msg = f'(L008) entry does not have all the required columns (have {current_segments_num}, need {num_segments})'

        self.assertIsInstance(err_msgs, list)
        self.assertEqual(len(err_msgs), 1)
        err_msg = err_msgs[0]
        self.assertEqual(err_msg, expected_err_msg)

    def test_check_file_format_without_1_space_between_the_segments(self):
        incorrect_format = [
            '## Index',
            '* [A](#a)',
            '',
            '### A',
            'API | Description | Auth | HTTPS | CORS |',
            '|---|---|---|---|---|',
            '| [AA](https://www.ex.com) | Desc |`apiKey`| Yes | Yes |',  # space between segment of auth column missing
            '| [AB](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '| [AC](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
        ]

        err_msgs = check_file_format(lines=incorrect_format)
        expected_err_msg = f'(L007) each segment must start and end with exactly 1 space'

        self.assertIsInstance(err_msgs, list)
        self.assertEqual(len(err_msgs), 1)
        err_msg = err_msgs[0]
        self.assertEqual(err_msg, expected_err_msg)

    # --- Markdown alignment rows are table chrome, not API entries ---

    def test_is_separator_row_accepts_markdown_alignment_variants(self):
        separators = [
            '|---|---|---|---|---|',
            '|:---|:---|:---|:---|:---|',
            '|---:|---:|---:|---:|---:|',
            '|:---:|:---:|:---:|:---:|:---:|',
            '| --- | --- | --- | --- | --- |',
            '| :--- | ---: | :---: | --- | :--- |',
        ]

        for separator in separators:
            with self.subTest(separator=separator):
                self.assertTrue(is_separator_row(separator))

        not_separators = [
            '| [AA](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '|:--|:--|:--|:--|:--|',
            '| Name | Description | Auth | Transport | Install |',
        ]

        for line in not_separators:
            with self.subTest(line=line):
                self.assertFalse(is_separator_row(line))

    def test_check_file_format_ignores_separator_variants(self):
        separators = [
            '|---|---|---|---|---|',
            '|:---|:---|:---|:---|:---|',
            '|---:|---:|---:|---:|---:|',
            '|:---:|:---:|:---:|:---:|:---:|',
            '| --- | --- | --- | --- | --- |',
        ]

        for separator in separators:
            with self.subTest(separator=separator):
                lines = [
                    '## Index',
                    '* [A](#a)',
                    '',
                    '### A',
                    'API | Description | Auth | HTTPS | CORS |',
                    separator,
                    '| [AA](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
                    '| [AB](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
                    '| [AC](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
                ]

                self.assertEqual(check_file_format(lines=lines), [])

    def test_check_file_format_still_rejects_invalid_row_after_separator(self):
        lines = [
            '## Index',
            '* [A](#a)',
            '',
            '### A',
            'API | Description | Auth | HTTPS | CORS |',
            '|:---|:---|:---|:---|:---|',
            '| [AA](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '| [AB](https://www.ex.com) | Desc | `apiKey` | Maybe | Sometimes |',
            '| [AC](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
        ]

        err_msgs = check_file_format(lines=lines)

        self.assertIn('(L008) Maybe is not a valid HTTPS option', err_msgs)
        self.assertIn('(L008) Sometimes is not a valid CORS option', err_msgs)

    # --- MCP server tables use Name/Description/Auth/Transport/Install ---

    def test_get_header_table_kind(self):
        self.assertEqual(get_header_table_kind('| API | Description | Auth | HTTPS | CORS |'), rest_table)
        self.assertEqual(get_header_table_kind('| Name | Description | Auth | Transport | Install |'), mcp_table)
        self.assertEqual(get_header_table_kind('| API | Description | Call this API |'), sponsored_table)
        self.assertIsNone(get_header_table_kind('| [AA](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |'))

    def test_check_mcp_entry_with_valid_row(self):
        valid = [
            '[Filesystem](https://github.com/modelcontextprotocol/servers)',
            'Read or write local files',
            'No',
            '`stdio`',
            '\u2013',
        ]

        self.assertEqual(check_mcp_entry(0, valid), [])

        for transport in transport_keys:
            with self.subTest(transport=transport):
                segments = list(valid)
                segments[3] = f'`{transport}`'
                self.assertEqual(check_mcp_entry(0, segments), [])

    def test_check_mcp_entry_rejects_invalid_values(self):
        valid = [
            '[Filesystem](https://github.com/modelcontextprotocol/servers)',
            'Read or write local files',
            'No',
            '`stdio`',
            '\u2013',
        ]

        invalid_transport = list(valid)
        invalid_transport[3] = '`Foo`'
        self.assertEqual(
            check_mcp_entry(0, invalid_transport),
            ['(L001) `Foo` is not a valid Transport option']
        )

        invalid_auth = list(valid)
        invalid_auth[2] = '`Bogus`'
        self.assertEqual(
            check_mcp_entry(0, invalid_auth),
            ['(L001) `Bogus` is not a valid Auth option']
        )

        empty_description = list(valid)
        empty_description[1] = ''
        self.assertEqual(
            check_mcp_entry(0, empty_description),
            ['(L001) description should not be empty']
        )

        invalid_install = list(valid)
        invalid_install[4] = 'somewhere'
        self.assertEqual(
            check_mcp_entry(0, invalid_install),
            ['(L001) somewhere is not a valid Install option']
        )

    def test_check_mcp_entry_enforces_description_length(self):
        long_desc = 'Desc' * max_description_length
        segments = [
            '[Filesystem](https://github.com/modelcontextprotocol/servers)',
            long_desc,
            'No',
            '`stdio`',
            '\u2013',
        ]

        self.assertEqual(
            check_mcp_entry(0, segments),
            [f'(L001) description should not exceed {max_description_length} characters (currently {len(long_desc)})']
        )

    def test_check_file_format_validates_mcp_table_with_mcp_columns(self):
        lines = [
            '## MCP Servers',
            '',
            '| Name | Description | Auth | Transport | Install |',
            '|:---|:---|:---|:---|:---|',
            '| [Filesystem](https://github.com/modelcontextprotocol/servers) | Read or write local files | No | `stdio` | \u2013 |',
            '| [GitHub MCP](https://github.com/github/github-mcp-server) | Repos, issues, PRs and code search | `OAuth` | `stdio`, `HTTP` | [Glama](https://glama.ai/mcp/servers/@github/github-mcp-server) |',
            '| [Kuro](https://meetkuro.com/agents/) | Create images, video clips and voice-overs | `OAuth` | `HTTP` | \u2013 |',
            '| [RegSentry](https://regsentry.com/mcp-guide) | Inspect tracking signals and consent evidence | No | `SSE` | [Anthropic](https://claude.ai/directory/regsentry) \u00b7 [Glama](https://glama.ai/mcp/servers/regsentry) |',
        ]

        self.assertEqual(check_file_format(lines=lines), [])

    def test_check_file_format_rejects_invalid_mcp_row_without_https_or_cors(self):
        lines = [
            '## MCP Servers',
            '',
            '| Name | Description | Auth | Transport | Install |',
            '|:---|:---|:---|:---|:---|',
            '| [Filesystem](https://github.com/modelcontextprotocol/servers) | Read or write local files | `Bogus` | `Foo` | \u2013 |',
        ]

        err_msgs = check_file_format(lines=lines)

        self.assertIn('(L005) `Bogus` is not a valid Auth option', err_msgs)
        self.assertIn('(L005) `Foo` is not a valid Transport option', err_msgs)
        self.assertFalse(any('HTTPS option' in msg or 'CORS option' in msg for msg in err_msgs))

    def test_check_file_format_rejects_mcp_row_with_missing_column(self):
        lines = [
            '## MCP Servers',
            '',
            '| Name | Description | Auth | Transport | Install |',
            '|:---|:---|:---|:---|:---|',
            '| [Filesystem](https://github.com/modelcontextprotocol/servers) | Read or write local files | No | `stdio` |',
        ]

        self.assertEqual(
            check_file_format(lines=lines),
            [f'(L005) entry does not have all the required columns (have 4, need {num_segments})']
        )

    # --- Prefatory/sponsored sections must not be read as indexed REST categories ---

    def test_check_file_format_separates_sponsored_preface_table(self):
        lines = [
            '## APILayer APIs',
            '| API | Description | Call this API |',
            '|:---|:---|:---|',
            '| [IPstack](https://ipstack.com) | Locate website visitors by IP address | [Postman](https://www.postman.com) |',
            '| [Fixer](https://fixer.io) | Foreign exchange rates | [Postman](https://www.postman.com) |',
            '',
            '## Index',
            '* [A](#a)',
            '',
            '### A',
            'API | Description | Auth | HTTPS | CORS |',
            '|:---|:---|:---|:---|:---|',
            '| [AA](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '| [AB](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '| [AC](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
        ]

        self.assertEqual(check_file_format(lines=lines), [])

    def test_check_file_format_prefatory_heading_without_rest_table_is_not_a_category(self):
        lines = [
            '# Sponsors',
            '### APIs Covered Under APILayer Suite!',
            '',
            '- [IPstack](https://ipstack.com)',
            '- [Fixer](https://fixer.io)',
            '',
            '## Index',
            '* [A](#a)',
            '',
            '### A',
            'API | Description | Auth | HTTPS | CORS |',
            '|:---|:---|:---|:---|:---|',
            '| [AA](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '| [AB](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '| [AC](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
        ]

        self.assertEqual(check_file_format(lines=lines), [])

    def test_check_file_format_top_level_section_does_not_contaminate_category_count(self):
        lines = [
            '## Index',
            '* [A](#a)',
            '* [B](#b)',
            '',
            '### A',
            'API | Description | Auth | HTTPS | CORS |',
            '|:---|:---|:---|:---|:---|',
            '| [AA](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '| [AB](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '',
            '## MCP Servers',
            '| Name | Description | Auth | Transport | Install |',
            '|:---|:---|:---|:---|:---|',
            '| [Zulu](https://www.ex.com) | Desc | No | `stdio` | \u2013 |',
            '',
            '### B',
            'API | Description | Auth | HTTPS | CORS |',
            '|:---|:---|:---|:---|:---|',
            '| [BA](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '| [BB](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '| [BC](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
        ]

        self.assertEqual(
            check_file_format(lines=lines),
            [f'(L005) A category does not have the minimum {min_entries_per_category} entries (only has 2)']
        )

    # --- REST rows keep being validated even without an explicit header ---

    def test_check_file_format_validates_rows_when_header_is_absent(self):
        lines = [
            '## Index',
            '* [A](#a)',
            '',
            '### A',
            '| [AA](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '| [AB](https://www.ex.com) | Desc | `apiKey` | Maybe | Yes |',
            '| [AC](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
        ]

        self.assertEqual(check_file_format(lines=lines), ['(L006) Maybe is not a valid HTTPS option'])

    # --- Sabotage guards: these must keep failing if the REST checks are weakened ---

    def test_check_file_format_rejects_invalid_rest_auth_https_cors(self):
        lines = [
            '## Index',
            '* [A](#a)',
            '',
            '### A',
            'API | Description | Auth | HTTPS | CORS |',
            '|:---|:---|:---|:---|:---|',
            '| [AA](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '| [AB](https://www.ex.com) | Desc | Bogus | Maybe | Sometimes |',
            '| [AC](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
        ]

        err_msgs = check_file_format(lines=lines)

        self.assertIn('(L008) auth value is not enclosed with `backticks`', err_msgs)
        self.assertIn('(L008) Bogus is not a valid Auth option', err_msgs)
        self.assertIn('(L008) Maybe is not a valid HTTPS option', err_msgs)
        self.assertIn('(L008) Sometimes is not a valid CORS option', err_msgs)

    def test_check_file_format_detects_unsorted_rest_category(self):
        lines = [
            '## Index',
            '* [A](#a)',
            '',
            '### A',
            'API | Description | Auth | HTTPS | CORS |',
            '|:---|:---|:---|:---|:---|',
            '| [AB](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '| [AA](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
            '| [AC](https://www.ex.com) | Desc | `apiKey` | Yes | Yes |',
        ]

        self.assertEqual(check_file_format(lines=lines), ['(L004) A category is not alphabetical order'])
