# -*- coding: utf-8 -*-

from email import message
import unittest

from validate.format import error_message
from validate.format import get_categories_content
from validate.format import check_alphabetical_order


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
