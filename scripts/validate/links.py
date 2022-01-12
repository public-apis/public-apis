# -*- coding: utf-8 -*-

import re
import sys
import random
from typing import List, Tuple

import requests


def find_links_in_text(text: str) -> List[str]:
    """Find links in a text and return a list of URLs."""

    link_pattern = re.compile(r'((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'\".,<>?«»“”‘’]))')

    raw_links = re.findall(link_pattern, text)

    links = [
        str(raw_link[0]).rstrip('/') for raw_link in raw_links
    ]

    return links


def find_links_in_file(filename: str) -> List[str]:
    """Find links in a file and return a list of URLs from text file."""

    with open(filename, mode='r', encoding='utf-8') as file:
        readme = file.read()
        index_section = readme.find('## Index')
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

    host = link.split('://', 1)[1]

    # Remove routes, arguments and anchors
    if '/' in host:
        host = host.split('/', 1)[0]

    elif '?' in host:
        host = host.split('?', 1)[0]

    elif '#' in host:
        host = host.split('#', 1)[0]

    return host


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
        resp = requests.get(link + '/', timeout=25, headers={
            'User-Agent': fake_user_agent(),
            'host': get_host_from_link(link)
        })

        code = resp.status_code
        if code >= 400:
            has_error = True
            error_message = f'ERR:CLT: {code} : {link}'

    except (TimeoutError, requests.exceptions.ConnectTimeout):
        has_error = True
        error_message = f'ERR:TMO: {link}'
    
    except requests.exceptions.SSLError as error:
        has_error = True
        error_message = f'ERR:SSL: {error} : {link}'
    
    except requests.exceptions.TooManyRedirects as error:
        has_error = True
        error_message = f'ERR:TMR: {error} : {link}'

    except Exception as error:
        has_error = True
        error_message = f'ERR:UKN: {error} : {link}'
    
    return (has_error, error_message)


if __name__ == '__main__':
    num_args = len(sys.argv)

    if num_args < 2:
        print('No .md file passed')
        sys.exit(1)

    links = find_links_in_file(sys.argv[1])

    print('Checking for duplicate links...')

    has_duplicate_link, duplicates_links = check_duplicate_links(links)

    if has_duplicate_link:
        print(f'Found duplicate links: {duplicates_links}')
    else:
        print('No duplicate links.')
