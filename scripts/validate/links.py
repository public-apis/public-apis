# -*- coding: utf-8 -*-

import re
import sys
import random
from typing import List, Tuple

import requests
from requests.models import Response


def find_links_in_text(text: str) -> List[str]:
    """Find links in a text and return a list of URLs."""

    link_pattern = re.compile(r'((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'\".,<>?«»“”‘’]))')

    raw_links = re.findall(link_pattern, text)

    links = [
        str(raw_link[0]) for raw_link in raw_links
    ]

    return links


def find_links_in_file(filename: str) -> List[str]:
    """Find links in a file and return a list of URLs from text file."""

    with open(filename, mode='r', encoding='utf-8') as file:
        readme = file.read()
        index_section = readme.find('## Index')
        if index_section == -1:
            index_section = 0
        content = readme[index_section:]

    links = find_links_in_text(content)

    return links


def check_duplicate_links(links: List[str]) -> Tuple[bool, List]:
    """Check for duplicated links.

    Returns a tuple with True or False and duplicate list.
    """

    seen = {}
    duplicates = []
    has_duplicate = False

    for link in links:
        link = link.rstrip('/')
        if link not in seen:
            seen[link] = 1
        else:
            if seen[link] == 1:
                duplicates.append(link)

    if duplicates:
        has_duplicate = True

    return (has_duplicate, duplicates)


def fake_user_agent() -> str:
    """Faking user agent as some hosting services block not-whitelisted UA."""

    user_agents = [
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko)',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    ]

    return random.choice(user_agents)


def get_host_from_link(link: str) -> str:

    host = link.split('://', 1)[1] if '://' in link else link

    # Remove routes, arguments and anchors
    if '/' in host:
        host = host.split('/', 1)[0]

    elif '?' in host:
        host = host.split('?', 1)[0]

    elif '#' in host:
        host = host.split('#', 1)[0]

    return host


def has_cloudflare_protection(resp: Response) -> bool:
    """Checks if there is any cloudflare protection in the response.

    Cloudflare implements multiple network protections on a given link,
    this script tries to detect if any of them exist in the response from request.

    Common protections have the following HTTP code as a response:
        - 403: When host header is missing or incorrect (and more)
        - 503: When DDOS protection exists

    See more about it at:
        - https://support.cloudflare.com/hc/en-us/articles/115003014512-4xx-Client-Error
        - https://support.cloudflare.com/hc/en-us/articles/115003011431-Troubleshooting-Cloudflare-5XX-errors
        - https://www.cloudflare.com/ddos/
        - https://superuser.com/a/888526

    Discussions in issues and pull requests:
        - https://github.com/public-apis/public-apis/pull/2409
        - https://github.com/public-apis/public-apis/issues/2960 
    """

    code = resp.status_code
    server = resp.headers.get('Server') or resp.headers.get('server')
    cloudflare_flags = [
        '403 Forbidden',
        'cloudflare',
        'Cloudflare',
        'Security check',
        'Please Wait... | Cloudflare',
        'We are checking your browser...',
        'Please stand by, while we are checking your browser...',
        'Checking your browser before accessing',
        'This process is automatic.',
        'Your browser will redirect to your requested content shortly.',
        'Please allow up to 5 seconds',
        'DDoS protection by',
        'Ray ID:',
        'Cloudflare Ray ID:',
        '_cf_chl',
        '_cf_chl_opt',
        '__cf_chl_rt_tk',
        'cf-spinner-please-wait',
        'cf-spinner-redirecting'
    ]

    if code in [403, 503] and server == 'cloudflare':
        html = resp.text

        flags_found = [flag in html for flag in cloudflare_flags]
        any_flag_found = any(flags_found)

        if any_flag_found:
            return True

    return False


def check_if_link_is_working(link: str) -> Tuple[bool, str]:
    """Checks if a link is working.

    If an error is identified when the request for the link occurs,
    the return will be a tuple with the first value True and the second
    value a string containing the error message.

    If no errors are identified, the return will be a tuple with the
    first value False and the second an empty string.
    """

    has_error = False
    error_message = ''

    try:
        resp = requests.get(link, timeout=25, headers={
            'User-Agent': fake_user_agent(),
            'host': get_host_from_link(link)
        })

        code = resp.status_code

        if code >= 400 and not has_cloudflare_protection(resp):
            has_error = True
            error_message = f'ERR:CLT: {code} : {link}'

    except requests.exceptions.SSLError as error:
        has_error = True
        error_message = f'ERR:SSL: {error} : {link}'

    except requests.exceptions.ConnectionError as error:
        has_error = True
        error_message = f'ERR:CNT: {error} : {link}'

    except (TimeoutError, requests.exceptions.ConnectTimeout):
        has_error = True
        error_message = f'ERR:TMO: {link}'

    except requests.exceptions.TooManyRedirects as error:
        has_error = True
        error_message = f'ERR:TMR: {error} : {link}'

    except (Exception, requests.exceptions.RequestException) as error:
        has_error = True
        error_message = f'ERR:UKN: {error} : {link}'

    return (has_error, error_message)


def check_if_list_of_links_are_working(list_of_links: List[str]) -> List[str]:
    error_messages = []
    for link in list_of_links:
        has_error, error_message = check_if_link_is_working(link)

        if has_error:
            error_messages.append(error_message)

    return error_messages


def start_duplicate_links_checker(links: List[str]) -> None:

    print('Checking for duplicate links...')

    has_duplicate_link, duplicates_links = check_duplicate_links(links)

    if has_duplicate_link:
        print(f'Found duplicate links:')

        for duplicate_link in duplicates_links:
            print(duplicate_link)

        sys.exit(1)
    else:
        print('No duplicate links.')


# ---------------------------------------------------------------------------
# Refined "-odlc" duplicate check: table-aware, function-row based.
# ---------------------------------------------------------------------------

# Local copy of the 5-column table header used by scripts/validate/format.py so
# this check stays decoupled from format.py.
_TABLE_HEADER = '| Function | Header | Description | Standard | MT-Safe |'

# Matches a Markdown link in the Function column: [name](url)
_FUNC_LINK_RE = re.compile(
    r'^\[([a-zA-Z_][a-zA-Z0-9_]*)\]\((https?://[^)]+)\)$'
)


def _parse_table_row(line: str) -> List[str] | None:
    """Parse a 5-column function-table data row, or return None if not one."""
    if not line.startswith('|'):
        return None
    if line.startswith('|---') or _TABLE_HEADER in line:
        return None
    parts = line.split('|')
    if len(parts) != 7:
        return None
    return [p.strip() for p in parts[1:-1]]


def check_duplicate_function_rows(filename: str) -> Tuple[bool, List[str]]:
    """Detect *true* redundant function rows in the 5-column tables.

    Unlike the URL-level :func:`check_duplicate_links`, this only flags genuine
    copy-paste redundancy: a function-table row whose full text is duplicated
    elsewhere in the document. Legal cases are intentionally ignored:

    * Different function names pointing at the same man7 manual page (e.g.
      ``wait(2)`` is referenced by several distinct functions) are *not*
      flagged, because the function names differ.
    * The same function reused across modules with a different MT-Safe note
      (e.g. ``strerror``) is *not* flagged, because its rows are not identical.

    Returns ``(has_duplicate, messages)``. No function rows are ever removed.
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        lines = [ln.rstrip('\n') for ln in f]

    seen: dict[str, List[dict]] = {}
    current_module: str | None = None

    for line_number, raw in enumerate(lines, start=1):
        stripped = raw.strip()
        if stripped.startswith('## '):
            title = stripped[3:].strip()
            current_module = None if title.lower() == 'index' else title
            continue
        if not stripped.startswith('|'):
            continue
        cols = _parse_table_row(stripped)
        if cols is None:
            continue
        func_cell = cols[0]
        match = _FUNC_LINK_RE.match(func_cell)
        if not match:
            continue
        func_name, url = match.group(1), match.group(2)
        # The full normalized row text is the duplication key. Two identical
        # rows necessarily share the same function name and URL, while the
        # legal shared-page / cross-module cases have differing row text.
        seen.setdefault(stripped, []).append({
            'func': func_name,
            'url': url,
            'module': current_module,
            'line': line_number,
        })

    duplicates: List[str] = []
    for key, occurrences in seen.items():
        if len(occurrences) < 2:
            continue
        func = occurrences[0]['func']
        url = occurrences[0]['url']
        locs = ', '.join(
            f'line {o["line"]}' + (f' ({o["module"]})' if o["module"] else '')
            for o in occurrences
        )
        duplicates.append(
            f'Duplicate function row for "{func}" ({url}) at {locs}'
        )

    return (len(duplicates) > 0, duplicates)


def start_function_duplicate_checker(filename: str) -> None:
    """Table-aware duplicate checker used by the ``-odlc`` flag.

    Only *true* redundant function rows are reported (see
    :func:`check_duplicate_function_rows`). The exit code stays hard (1 on
    duplicates) so the CI gate can keep ``continue-on-error: true`` and remain
    a soft, non-blocking check.
    """
    print('Checking for duplicate function rows...')
    has_duplicate, duplicates = check_duplicate_function_rows(filename)
    if has_duplicate:
        print('Found duplicate function rows:')
        for duplicate in duplicates:
            print(duplicate)
        sys.exit(1)
    else:
        print('No duplicate function rows.')


def start_links_working_checker(links: List[str]) -> None:

    print(f'Checking if {len(links)} links are working...')

    errors = check_if_list_of_links_are_working(links)
    if errors:

        num_errors = len(errors)
        print(f'Apparently {num_errors} links are not working properly. See in:')

        for error_message in errors:
            print(error_message)

        sys.exit(1)


def main(filename: str, only_duplicate_links_checker: bool) -> None:

    if only_duplicate_links_checker:
        # Refined, table-aware duplicate check (soft gate at workflow level).
        start_function_duplicate_checker(filename)
        return

    links = find_links_in_file(filename)

    start_duplicate_links_checker(links)

    if not only_duplicate_links_checker:
        start_links_working_checker(links)


if __name__ == '__main__':
    num_args = len(sys.argv)
    only_duplicate_links_checker = False

    if num_args < 2:
        print('No .md file passed')
        sys.exit(1)
    elif num_args == 3:
        third_arg = sys.argv[2].lower()

        if third_arg == '-odlc' or third_arg == '--only_duplicate_links_checker':
            only_duplicate_links_checker = True
        else:
            print(f'Third invalid argument. Usage: python {__file__} [-odlc | --only_duplicate_links_checker]')
            sys.exit(1)

    filename = sys.argv[1]

    main(filename, only_duplicate_links_checker)
