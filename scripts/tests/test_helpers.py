# -*- coding: utf-8 -*-

"""Shared sample Markdown fixtures for the validate package test suite.

These fragments use the current 5-column schema
(Function | Header | Description | Standard | MT-Safe) so the tests stay in
sync with ``scripts/validate/format.py``.
"""

# A minimal but valid README: an Index plus two modules, no duplicates,
# matching anchors. Used to assert the happy path.
VALID_README = """# glibc — 公共 API 索引

## Index

* [Standard I/O (stdio.h)](#standard-io-stdioh)
* [Math Library (math.h)](#math-library-mathh)

---

## Standard I/O (stdio.h)

### Stream Open/Close

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [fopen](https://man7.org/linux/man-pages/man3/fopen.3.html) | `<stdio.h>` | Open a file and associate a stream with it | POSIX.1-2001, C89 | Yes |
| [fclose](https://man7.org/linux/man-pages/man3/fclose.3.html) | `<stdio.h>` | Flush and close a stream | POSIX.1-2001, C89 | Yes |

## Math Library (math.h)

### Trigonometry

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [sin](https://man7.org/linux/man-pages/man3/sin.3.html) | `<math.h>` | Compute the sine of an angle | C99 | Yes |
"""

# Same function listed twice inside one module -> error.
DUP_FUNCTION_README = """# glibc

## Index

* [Math Library (math.h)](#math-library-mathh)

---

## Math Library (math.h)

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [sin](https://man7.org/linux/man-pages/man3/sin.3.html) | `<math.h>` | Compute the sine of an angle | C99 | Yes |
| [sin](https://man7.org/linux/man-pages/man3/sin.3.html) | `<math.h>` | Compute the sine of an angle | C99 | Yes |
"""

# Index anchor set diverges from the module heading because the heading uses
# the HTML entity '&amp;' instead of '&'. This reproduces the real broken-link
# bug and must be caught by check_index_sync.
INDEX_MISMATCH_README = """# glibc

## Index

* [Environment & System Info (unistd.h)](#environment--system-info-unistdh-sysutsnameh)

---

## Environment &amp; System Info (unistd.h, sys/utsname.h)

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [getenv](https://man7.org/linux/man-pages/man3/getenv.3.html) | `<stdlib.h>` | Get an environment variable | POSIX.1-2001 | Yes |
"""

# The same function appears in two *different* modules with conflicting MT-Safe
# values -> warning (not an error, because cross-module reuse is allowed).
MTSAFE_MISMATCH_README = """# glibc

## Index

* [Error Handling (errno.h)](#error-handling-errnoh)
* [Locale (locale.h)](#locale-localeh)

---

## Error Handling (errno.h)

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [strerror](https://man7.org/linux/man-pages/man3/strerror.3.html) | `<string.h>` | Return a string describing an error | POSIX.1-2001 | Yes |

## Locale (locale.h)

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [strerror](https://man7.org/linux/man-pages/man3/strerror.3.html) | `<string.h>` | Return a string describing an error | POSIX.1-2001 | No (race:strerror locale) |
"""
