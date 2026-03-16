# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch

from validate.apis import ApiEntry
from validate.apis import has_free_tier_signal
from validate.apis import find_entries_to_remove
from validate.apis import parse_api_entries
from validate.apis import remove_entries_from_lines


class TestValidateApis(unittest.TestCase):

    def test_parse_api_entries(self):
        lines = [
            '| [Cat Facts](https://example.com/cats) | Free cat facts | No | Yes | Yes |',
            '| [Dog Facts](https://example.com/dogs) | Premium data only | `apiKey` | Yes | Yes |',
            '| Not an API line |',
        ]

        entries = parse_api_entries(lines)

        self.assertEqual(len(entries), 2)
        self.assertEqual(entries[0].title, 'Cat Facts')
        self.assertEqual(entries[0].link, 'https://example.com/cats')
        self.assertEqual(entries[0].auth, 'no')

    def test_has_free_tier_signal(self):
        free_entry_auth = ApiEntry(1, '', 'A', 'Paid service', 'no', 'https://example.com')
        free_entry_desc = ApiEntry(2, '', 'B', 'This API has a free tier for hobby usage', 'apikey', 'https://example.com')
        paid_entry = ApiEntry(3, '', 'C', 'Enterprise pricing only', 'apikey', 'https://example.com')

        self.assertTrue(has_free_tier_signal(free_entry_auth))
        self.assertTrue(has_free_tier_signal(free_entry_desc))
        self.assertFalse(has_free_tier_signal(paid_entry))


    @patch('validate.apis.check_if_link_is_working', return_value=(True, 'ERR'))
    def test_find_entries_to_remove_counts_link_failures(self, _):
        entries = [
            ApiEntry(1, '', 'A', 'Free tier', 'apikey', 'https://example.com/a'),
            ApiEntry(2, '', 'B', 'Paid only', 'apikey', 'https://example.com/b'),
        ]

        to_remove, report, link_failures = find_entries_to_remove(entries)

        self.assertEqual(len(to_remove), 2)
        self.assertEqual(len(report), 2)
        self.assertEqual(link_failures, 2)

    def test_remove_entries_from_lines(self):
        lines = ['line 1', 'line 2', 'line 3']
        entries_to_remove = [
            ApiEntry(2, 'line 2', 'X', 'Y', 'no', 'https://example.com')
        ]

        result = remove_entries_from_lines(lines, entries_to_remove)

        self.assertEqual(result, ['line 1', 'line 3'])


if __name__ == '__main__':
    unittest.main()
