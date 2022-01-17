# -*- coding: utf-8 -*-

import unittest

from validate.format import error_message
from validate.format import get_categories_content
from validate.format import check_alphabetical_order
from validate.format import check_title
from validate.format import check_description, max_description_length


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

    def test_check_title_return_type(self):
        raw_title_1 = '[A](https://www.ex.com)'
        raw_title_2 = '[A(https://www.ex.com)'
        raw_title_3 = '[A API](https://www.ex.com)'

        result_1 = check_title(0, raw_title_1)
        result_2 = check_title(0, raw_title_2)
        result_3 = check_title(0, raw_title_3)

        self.assertIsInstance(result_1, list)
        self.assertIsInstance(result_2, list)
        self.assertIsInstance(result_3, list)

        err_msg_1 = result_2[0]
        err_msg_2 = result_3[0]

        self.assertIsInstance(err_msg_1, str)
        self.assertIsInstance(err_msg_2, str)
    
    def test_check_title_with_correct_title(self):
        raw_title = '[A](https://www.ex.com)'

        err_msgs = check_title(0, raw_title)

        self.assertEqual(len(err_msgs), 0)
        
        self.assertEqual(err_msgs, [])

    def test_check_title_with_markdown_syntax_incorrect(self):
        raw_title = '[A(https://www.ex.com)'

        err_msgs = check_title(0, raw_title)

        self.assertEqual(len(err_msgs), 1)
        
        err_msg = err_msgs[0]
        expected_err_msg = '(L001) Title syntax should be "[TITLE](LINK)"'

        self.assertEqual(err_msg, expected_err_msg)

    def test_check_title_with_api_at_the_end_of_the_title(self):
        raw_title = '[A API](https://www.ex.com)'

        err_msgs = check_title(0, raw_title)

        self.assertEqual(len(err_msgs), 1)
        
        err_msg = err_msgs[0]
        expected_err_msg = '(L001) Title should not end with "... API". Every entry is an API here!'

        self.assertEqual(err_msg, expected_err_msg)

    def test_checK_description_return_type(self):
        desc_1 = 'This is a fake description'
        desc_2 = 'this is a fake description'
        desc_3 = 'This is a fake description!'
        desc_4 = 'This is a fake descriptionThis is a fake descriptionThis is a fake descriptionThis is a fake description'

        result_1 = check_title(0, desc_1)
        result_2 = check_title(0, desc_2)
        result_3 = check_title(0, desc_3)
        result_4 = check_title(0, desc_4)

        self.assertIsInstance(result_1, list)
        self.assertIsInstance(result_2, list)
        self.assertIsInstance(result_3, list)
        self.assertIsInstance(result_4, list)

        err_msg_1 = result_2[0]
        err_msg_2 = result_3[0]
        err_msg_3 = result_4[0]

        self.assertIsInstance(err_msg_1, str)
        self.assertIsInstance(err_msg_2, str)
        self.assertIsInstance(err_msg_3, str)

    def test_check_description_with_correct_description(self):
        desc = 'This is a fake description'

        err_msgs = check_description(0, desc)

        self.assertEqual(len(err_msgs), 0)

        self.assertEqual(err_msgs, [])
    
    def test_check_description_with_first_char_is_not_capitalized(self):
        desc = 'this is a fake description'

        err_msgs = check_description(0, desc)

        self.assertEqual(len(err_msgs), 1)
        
        err_msg = err_msgs[0]
        expected_err_msg = '(L001) first character of description is not capitalized'

        self.assertEqual(err_msg, expected_err_msg)
    
    def test_check_description_with_punctuation_in_the_end(self):
        base_desc = 'This is a fake description'
        punctuation = r"""!"#$%&'*+,-./:;<=>?@[\]^_`{|}~"""
        desc_with_punc = [base_desc + punc for punc in punctuation]
        
        for desc in desc_with_punc:

            with self.subTest():
                err_msgs = check_description(0, desc)

                self.assertEqual(len(err_msgs), 1)
        
                err_msg = err_msgs[0]
                expected_err_msg = f'(L001) description should not end with {desc[-1]}'

                self.assertEqual(err_msg, expected_err_msg)

    def test_check_description_that_exceeds_the_character_limit(self):
        long_desc = 'Desc' * max_description_length
        long_desc_length = len(long_desc)

        err_msgs = check_description(0, long_desc)

        self.assertEqual(len(err_msgs), 1)

        err_msg = err_msgs[0]
        expected_err_msg = f'(L001) description should not exceed {max_description_length} characters (currently {long_desc_length})'

        self.assertEqual(err_msg, expected_err_msg)
