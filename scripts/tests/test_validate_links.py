# -*- coding: utf-8 -*-

import unittest

from validate.links import find_links_in_text
from validate.links import get_host_from_link


class TestValidateLinks(unittest.TestCase):

    def test_find_link_in_text(self):
        text = """
            # this is valid

            http://example.com?param1=1&param2=2#anchor
            https://www.example.com?param1=1&param2=2#anchor
            https://www.example.com.br
            https://www.example.com.gov.br
            [Example](https://www.example.com?param1=1&param2=2#anchor)
            lorem ipsum https://www.example.com?param1=1&param2=2#anchor
            https://www.example.com?param1=1&param2=2#anchor lorem ipsum

            # this not is valid

            example.com
            https:example.com
            https:/example.com
            https//example.com
            https//.com
        """

        links = find_links_in_text(text)

        self.assertIsInstance(links, list)
        self.assertEqual(len(links), 7)

        for link in links:
            with self.subTest():
                self.assertIsInstance(link, str)

    def test_find_link_in_text_with_invalid_argument(self):
        with self.assertRaises(TypeError):
            find_links_in_text()
            find_links_in_text(1)
            find_links_in_text(True)
    
    def test_get_host_from_link(self):
        links = [
            'example.com',
            'https://example.com',
            'https://www.example.com',
            'https://www.example.com.br',
            'https://www.example.com/route',
            'https://www.example.com?p=1&q=2',
            'https://www.example.com#anchor'
        ]

        for link in links:
            host = get_host_from_link(link)

            with self.subTest():
                self.assertIsInstance(host, str)

                self.assertNotIn('://', host)
                self.assertNotIn('/', host)
                self.assertNotIn('?', host)
                self.assertNotIn('#', host)

        with self.assertRaises(TypeError):
            get_host_from_link()
