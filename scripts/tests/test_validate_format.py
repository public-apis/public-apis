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
from validate.format import check_transport, check_install, check_mcp_entry


class TestValidadeFormat(unittest.TestCase):
    
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


class TestValidateMCPFormat(unittest.TestCase):
    def mcp_lines(self, rows):
        return [
            '## MCP Servers',
            '| Name | Description | Auth | Transport | Install |',
            '|:---|:---|:---|:---|:---|',
            *rows,
        ]

    def test_documented_mcp_table_accepts_http_and_install_links(self):
        rows = [
            '| [Alpha](https://example.com/alpha) | Read public records | No | `HTTP` | [Glama](https://glama.ai/mcp/connectors/example/alpha) |',
            '| [Beta](https://example.com/beta) | Read local files | `OAuth` | `stdio`, `SSE` | [Cursor](https://cursor.directory/plugins/beta) · [Anthropic](https://claude.ai/directory/beta) |',
            '| [Gamma](https://example.com/gamma) | Search records | No | `stdio` | – |',
        ]
        self.assertEqual(check_file_format(self.mcp_lines(rows)), [])

    def test_transports_require_documented_values_and_comma_separation(self):
        for transport in ['`stdio`', '`HTTP`', '`SSE`', '`stdio`, `HTTP`, `SSE`']:
            with self.subTest(transport=transport):
                self.assertEqual(check_transport(0, transport), [])
        for transport in ['Yes', 'HTTP', '`http`', '`WebSocket`', '`HTTP` `SSE`', '`HTTP`,`SSE`', '`HTTP`, ']:
            with self.subTest(transport=transport):
                self.assertEqual(len(check_transport(0, transport)), 1)

    def test_install_requires_documented_marketplace_links_or_en_dash(self):
        for install in [
            '–',
            '[Cursor](https://cursor.directory/plugins/alpha)',
            '[Anthropic](https://claude.ai/directory/alpha)',
            '[Glama](https://glama.ai/mcp/servers/@example/alpha)',
            '[Glama](https://glama.ai/mcp/connectors/example/alpha) · [Cursor](https://cursor.directory/plugins/alpha)',
        ]:
            with self.subTest(install=install):
                self.assertEqual(check_install(0, install), [])
        for install in [
            '-', 'Unknown', '',
            '[npm](https://www.npmjs.com/package/alpha)',
            '[Glama](https://example.com/alpha)',
            '[Glama](https://glama.ai.example.com/alpha)',
            '[Glama](http://glama.ai/mcp/servers/alpha)',
            '[Glama](https://[invalid)',
            '[Glama](https://glama.ai/mcp/servers/alpha), [Cursor](https://cursor.directory/plugins/alpha)',
            '[Glama](https://glama.ai/mcp/servers/alpha) · ',
        ]:
            with self.subTest(install=install):
                self.assertEqual(len(check_install(0, install)), 1)

    def test_mcp_preserves_shared_name_description_auth_and_spacing_rules(self):
        row = '| [Alpha API](https://example.com/alpha) | lowercase. | secret | `HTTP` | – |'
        errors = check_file_format(self.mcp_lines([row]))
        self.assertTrue(any('Title should not end' in error for error in errors))
        self.assertTrue(any('not capitalized' in error for error in errors))
        self.assertTrue(any('description should not end' in error for error in errors))
        self.assertTrue(any('not a valid Auth' in error for error in errors))
        spacing_errors = check_file_format(self.mcp_lines([
            '| [Alpha](https://example.com/alpha) | Desc |No| `HTTP` | – |',
        ]))
        self.assertTrue(any('exactly 1 space' in error for error in spacing_errors))

    def test_mcp_requires_exactly_five_columns(self):
        for row in [
            '| [Alpha](https://example.com/alpha) | Desc | No | `HTTP` |',
            '| [Alpha](https://example.com/alpha) | Desc | No | `HTTP` | – | Extra |',
            '|---|---|---|---|',
        ]:
            with self.subTest(row=row):
                errors = check_file_format(self.mcp_lines([row]))
                self.assertTrue(any('columns' in error for error in errors))

    def test_only_mcp_header_and_valid_separator_are_skipped(self):
        for separator in ['|---|---|---|---|---|', '| --- | --- | --- | --- | --- |', '|:---|---:|:---:|---|---|']:
            with self.subTest(separator=separator):
                self.assertEqual(check_file_format(['## MCP Servers', separator]), [])
        errors = check_file_format(['## MCP Servers', '| Name | Description | Auth | HTTPS | CORS |'])
        self.assertTrue(any('not a valid Transport' in error for error in errors))
        self.assertTrue(any('not a valid Install' in error for error in errors))

    def test_rest_schema_remains_strict_after_mcp_section(self):
        lines = self.mcp_lines([
            '| [Alpha](https://example.com/alpha) | Desc | No | `HTTP` | – |',
        ]) + [
            '## Index', '* [REST](#rest)', '### REST',
            'API | Description | Auth | HTTPS | CORS |', '|---|---|---|---|---|',
            '| [Alpha](https://example.com/alpha) | Desc | No | `HTTP` | [Glama](https://glama.ai/mcp/servers/alpha) |',
            '| [Beta](https://example.com/beta) | Desc | No | Yes | Yes |',
            '| [Gamma](https://example.com/gamma) | Desc | No | No | Unknown |',
        ]
        errors = check_file_format(lines)
        self.assertEqual(len(errors), 2)
        self.assertTrue(any('not a valid HTTPS' in error for error in errors))
        self.assertTrue(any('not a valid CORS' in error for error in errors))

    def test_level_one_heading_also_ends_mcp_section(self):
        lines = self.mcp_lines([]) + [
            '# REST', '* [REST](#rest)', '### REST',
            '| [Alpha](https://example.com/alpha) | Desc | No | Yes | Yes |',
            '| [Beta](https://example.com/beta) | Desc | No | No | No |',
            '| [Gamma](https://example.com/gamma) | Desc | No | Yes | Unknown |',
        ]
        self.assertEqual(check_file_format(lines), [])

    def test_mcp_subheading_does_not_change_transport_schema(self):
        lines = self.mcp_lines([]) + [
            '### Hosted servers',
            '| [Alpha](https://example.com/alpha) | Desc | No | `HTTP` | – |',
        ]
        self.assertEqual(check_file_format(lines), [])

    def test_mcp_ordering_is_separate_from_rest_categories(self):
        lines = [
            '## Index', '* [REST](#rest)', '### REST',
            '| [Alpha](https://example.com/alpha) | Desc | No | Yes | Yes |',
            '| [Beta](https://example.com/beta) | Desc | No | Yes | Yes |',
            '| [Gamma](https://example.com/gamma) | Desc | No | Yes | Yes |',
        ] + self.mcp_lines([
            '| [Beta](https://example.com/beta) | Desc | No | `HTTP` | – |',
            '| [Alpha](https://example.com/alpha) | Desc | No | `HTTP` | – |',
        ])
        self.assertEqual(check_file_format(lines), ['(L007) MCP Servers category is not alphabetical order'])

    def test_rest_entry_validator_does_not_accept_mcp_fields(self):
        segments = ['[Alpha](https://example.com/alpha)', 'Desc', 'No', '`HTTP`', '–']
        self.assertEqual(check_mcp_entry(0, segments), [])
        self.assertEqual(check_entry(0, segments), [
            '(L001) `HTTP` is not a valid HTTPS option',
            '(L001) – is not a valid CORS option',
        ])
