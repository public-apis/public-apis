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
