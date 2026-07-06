# -*- coding: utf-8 -*-

"""Unit tests for scripts/validate/links.py."""

import unittest

from validate.links import find_links_in_text
from validate.links import check_duplicate_links
from validate.links import check_duplicate_function_rows
from validate.links import fake_user_agent
from validate.links import get_host_from_link
from validate.links import has_cloudflare_protection
from validate.links import start_duplicate_links_checker


class FakeResponse():
    def __init__(self, code: int, headers: dict, text: str) -> None:
        self.status_code = code
        self.headers = headers
        self.text = text


class TestValidateLinks(unittest.TestCase):

    def setUp(self):
        self.duplicate_links = [
            'https://www.example.com',
            'https://www.example.com',
            'https://www.example.com',
            'https://www.anotherexample.com',
        ]
        self.no_duplicate_links = [
            'https://www.firstexample.com',
            'https://www.secondexample.com',
            'https://www.anotherexample.com',
        ]

        self.code_200 = 200
        self.code_403 = 403
        self.code_503 = 503

        self.cloudflare_headers = {'Server': 'cloudflare'}
        self.no_cloudflare_headers = {'Server': 'google'}

        self.text_with_cloudflare_flags = '403 Forbidden Cloudflare We are checking your browser...'
        self.text_without_cloudflare_flags = 'Lorem Ipsum'

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

    def test_if_check_duplicate_links_has_the_correct_return(self):
        result_1 = check_duplicate_links(self.duplicate_links)
        result_2 = check_duplicate_links(self.no_duplicate_links)

        self.assertIsInstance(result_1, tuple)
        self.assertIsInstance(result_2, tuple)

        has_duplicate_links, links = result_1
        no_duplicate_links, no_links = result_2

        self.assertTrue(has_duplicate_links)
        self.assertFalse(no_duplicate_links)

        self.assertIsInstance(links, list)
        self.assertIsInstance(no_links, list)

        self.assertEqual(len(links), 2)
        self.assertEqual(len(no_links), 0)

    def test_if_fake_user_agent_has_a_str_as_return(self):
        user_agent = fake_user_agent()
        self.assertIsInstance(user_agent, str)

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

    def test_has_cloudflare_protection_with_code_403_and_503_in_response(self):
        resp_with_cloudflare_protection_code_403 = FakeResponse(
            code=self.code_403,
            headers=self.cloudflare_headers,
            text=self.text_with_cloudflare_flags
        )

        resp_with_cloudflare_protection_code_503 = FakeResponse(
            code=self.code_503,
            headers=self.cloudflare_headers,
            text=self.text_with_cloudflare_flags
        )

        result1 = has_cloudflare_protection(resp_with_cloudflare_protection_code_403)
        result2 = has_cloudflare_protection(resp_with_cloudflare_protection_code_503)

        self.assertTrue(result1)
        self.assertTrue(result2)

    def test_has_cloudflare_protection_when_there_is_no_protection(self):
        resp_without_cloudflare_protection1 = FakeResponse(
            code=self.code_200,
            headers=self.no_cloudflare_headers,
            text=self.text_without_cloudflare_flags
        )

        resp_without_cloudflare_protection2 = FakeResponse(
            code=self.code_403,
            headers=self.no_cloudflare_headers,
            text=self.text_without_cloudflare_flags
        )

        resp_without_cloudflare_protection3 = FakeResponse(
            code=self.code_503,
            headers=self.no_cloudflare_headers,
            text=self.text_without_cloudflare_flags
        )

        result1 = has_cloudflare_protection(resp_without_cloudflare_protection1)
        result2 = has_cloudflare_protection(resp_without_cloudflare_protection2)
        result3 = has_cloudflare_protection(resp_without_cloudflare_protection3)

        self.assertFalse(result1)
        self.assertFalse(result2)
        self.assertFalse(result3)

    def test_start_duplicate_links_checker_exits_on_duplicates(self):
        # The duplicate-only checker must hard-fail when duplicate URLs exist.
        with self.assertRaises(SystemExit) as ctx:
            start_duplicate_links_checker(self.duplicate_links)
        self.assertEqual(ctx.exception.code, 1)

    def test_start_duplicate_links_checker_passes_on_unique_links(self):
        # With unique links it should not raise / exit.
        try:
            start_duplicate_links_checker(self.no_duplicate_links)
        except SystemExit:
            self.fail('start_duplicate_links_checker exited on unique links')


class TestCheckDuplicateFunctionRows(unittest.TestCase):
    """Regression tests for the refined -odlc table-aware duplicate check."""

    def _write_temp(self, text: str) -> str:
        import tempfile
        import os
        tf = tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8')
        tf.write(text)
        tf.close()
        self.addCleanup(os.unlink, tf.name)
        return tf.name

    def test_true_copy_paste_row_is_reported(self):
        # Two byte-identical rows for the same function -> genuine redundancy.
        readme = """# glibc

## Index

* [Math (math.h)](#math-mathh)

---

## Math (math.h)

### Trig

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [sin](https://man7.org/linux/man-pages/man3/sin.3.html) | `<math.h>` | Compute sine | C99 | Yes |
| [sin](https://man7.org/linux/man-pages/man3/sin.3.html) | `<math.h>` | Compute sine | C99 | Yes |
"""
        path = self._write_temp(readme)
        has_dup, dups = check_duplicate_function_rows(path)
        self.assertTrue(has_dup)
        self.assertEqual(len(dups), 1)
        self.assertIn('sin', dups[0])

    def test_different_functions_sharing_url_not_reported(self):
        # wait(2) referenced by distinct functions -> legal, must NOT flag.
        readme = """# glibc

## Index

* [Process (unistd.h)](#process-unistdh)

---

## Process (unistd.h)

### Wait

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [wait](https://man7.org/linux/man-pages/man2/wait.2.html) | `<sys/types.h>` | Wait for any child | POSIX.1-2001 | Yes |
| [waitpid](https://man7.org/linux/man-pages/man2/wait.2.html) | `<sys/types.h>` | Wait for a specific child | POSIX.1-2001 | Yes |
"""
        path = self._write_temp(readme)
        has_dup, dups = check_duplicate_function_rows(path)
        self.assertFalse(has_dup)
        self.assertEqual(dups, [])

    def test_same_function_cross_module_diff_rows_not_reported(self):
        # strerror-like: same name + url but different MT-Safe note -> legal.
        readme = """# glibc

## Index

* [Error (errno.h)](#error-errnoh)
* [Locale (locale.h)](#locale-localeh)

---

## Error (errno.h)

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [strerror](https://man7.org/linux/man-pages/man3/strerror.3.html) | `<string.h>` | Return a string describing an error | POSIX.1-2001 | Yes |

## Locale (locale.h)

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [strerror](https://man7.org/linux/man-pages/man3/strerror.3.html) | `<string.h>` | Return a string describing an error | POSIX.1-2001 | No (race:strerror locale) |
"""
        path = self._write_temp(readme)
        has_dup, dups = check_duplicate_function_rows(path)
        self.assertFalse(has_dup)
        self.assertEqual(dups, [])


if __name__ == '__main__':
    unittest.main()
