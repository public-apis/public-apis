# -*- coding: utf-8 -*-

import re
import sys
from string import punctuation
from typing import List, Tuple, Dict
from urllib.parse import urlsplit

# Temporary replacement
# The descriptions that contain () at the end must adapt to the new policy later
punctuation = punctuation.replace('()', '')

anchor = '###'
auth_keys = ['apiKey', 'OAuth', 'X-Mashape-Key', 'User-Agent', 'No']
https_keys = ['Yes', 'No']
cors_keys = ['Yes', 'No', 'Unknown']
mcp_title = 'MCP Servers'
mcp_header = ['Name', 'Description', 'Auth', 'Transport', 'Install']
transport_re = re.compile(r'`(?:stdio|HTTP|SSE)`(?:, `(?:stdio|HTTP|SSE)`)*')
install_link_re = re.compile(r'\[([^\]]+)\]\((https://[^\s()]+)\)')
install_hosts = {
    'Cursor': 'cursor.directory',
    'Anthropic': 'claude.ai',
    'Glama': 'glama.ai',
}

index_title = 0
index_desc = 1
index_auth = 2
index_https = 3
index_cors = 4
index_transport = 3
index_install = 4

num_segments = 5
min_entries_per_category = 3
max_description_length = 100

anchor_re = re.compile(anchor + '\s(.+)')
category_title_in_index_re = re.compile('\*\s\[(.*)\]')
link_re = re.compile('\[(.+)\]\((http.*)\)')

# Type aliases
APIList = List[str]
Categories = Dict[str, APIList]
CategoriesLineNumber = Dict[str, int]


def error_message(line_number: int, message: str) -> str:
    line = line_number + 1
    return f'(L{line:03d}) {message}'


def get_mcp_line_numbers(contents: List[str]) -> set:
    """The separately documented MCP table ends at the next level-1/2 heading."""
    line_numbers = set()
    in_mcp = False
    for line_num, line_content in enumerate(contents):
        heading = re.match(r'^(#{1,2})\s+(.+?)\s*$', line_content)
        if heading:
            in_mcp = heading.group(1) == '##' and heading.group(2) == mcp_title
        if in_mcp:
            line_numbers.add(line_num)
    return line_numbers


def get_categories_content(contents: List[str]) -> Tuple[Categories, CategoriesLineNumber]:

    categories = {}
    category_line_num = {}
    mcp_lines = get_mcp_line_numbers(contents)

    for line_num, line_content in enumerate(contents):

        if line_num in mcp_lines and re.fullmatch(r'##\s+MCP Servers\s*', line_content):
            categories[mcp_title] = []
            category_line_num[mcp_title] = line_num
            continue

        if line_num not in mcp_lines and line_content.startswith(anchor):
            category = line_content.split(anchor)[1].strip()
            categories[category] = []
            category_line_num[category] = line_num
            continue

        if not line_content.startswith('|') or line_content.startswith('|---'):
            continue

        raw_title = [
            raw_content.strip() for raw_content in line_content.split('|')[1:-1]
        ][0]

        title_match = link_re.match(raw_title)
        if title_match:
                title = title_match.group(1).upper()
                entry_category = mcp_title if line_num in mcp_lines else category
                categories[entry_category].append(title)

    return (categories, category_line_num)


def check_alphabetical_order(lines: List[str]) -> List[str]:

    err_msgs = []

    categories, category_line_num = get_categories_content(contents=lines)

    for category, api_list in categories.items():
        if sorted(api_list) != api_list:
            err_msg = error_message(
                category_line_num[category], 
                f'{category} category is not alphabetical order'
            )
            err_msgs.append(err_msg)
    
    return err_msgs


def check_title(line_num: int, raw_title: str) -> List[str]:

    err_msgs = []

    title_match = link_re.match(raw_title)

    # url should be wrapped in "[TITLE](LINK)" Markdown syntax
    if not title_match:
        err_msg = error_message(line_num, 'Title syntax should be "[TITLE](LINK)"')
        err_msgs.append(err_msg)
    else:
        # do not allow "... API" in the entry title
        title = title_match.group(1)
        if title.upper().endswith(' API'):
            err_msg = error_message(line_num, 'Title should not end with "... API". Every entry is an API here!')
            err_msgs.append(err_msg)

    return err_msgs


def check_description(line_num: int, description: str) -> List[str]:

    err_msgs = []

    first_char = description[0]
    if first_char.upper() != first_char:
        err_msg = error_message(line_num, 'first character of description is not capitalized')
        err_msgs.append(err_msg)

    last_char = description[-1]
    if last_char in punctuation:
        err_msg = error_message(line_num, f'description should not end with {last_char}')
        err_msgs.append(err_msg)

    desc_length = len(description)
    if desc_length > max_description_length:
        err_msg = error_message(line_num, f'description should not exceed {max_description_length} characters (currently {desc_length})')
        err_msgs.append(err_msg)
    
    return err_msgs


def check_auth(line_num: int, auth: str) -> List[str]:

    err_msgs = []

    backtick = '`'
    if auth != 'No' and (not auth.startswith(backtick) or not auth.endswith(backtick)):
        err_msg = error_message(line_num, 'auth value is not enclosed with `backticks`')
        err_msgs.append(err_msg)

    if auth.replace(backtick, '') not in auth_keys:
        err_msg = error_message(line_num, f'{auth} is not a valid Auth option')
        err_msgs.append(err_msg)
    
    return err_msgs


def check_https(line_num: int, https: str) -> List[str]:

    err_msgs = []

    if https not in https_keys:
        err_msg = error_message(line_num, f'{https} is not a valid HTTPS option')
        err_msgs.append(err_msg)

    return err_msgs


def check_cors(line_num: int, cors: str) -> List[str]:

    err_msgs = []

    if cors not in cors_keys:
        err_msg = error_message(line_num, f'{cors} is not a valid CORS option')
        err_msgs.append(err_msg)
    
    return err_msgs


def check_transport(line_num: int, transport: str) -> List[str]:
    if not transport_re.fullmatch(transport):
        return [error_message(line_num, f'{transport} is not a valid Transport option')]
    return []


def check_install(line_num: int, install: str) -> List[str]:
    if install == '–':
        return []
    for listing in install.split(' · '):
        match = install_link_re.fullmatch(listing)
        if match:
            try:
                url = urlsplit(match.group(2))
                if url.netloc == install_hosts.get(match.group(1)):
                    continue
            except ValueError:
                pass
        return [error_message(line_num, f'{install} is not a valid Install option')]
    return []


def check_mcp_entry(line_num: int, segments: List[str]) -> List[str]:
    return [
        *check_title(line_num, segments[index_title]),
        *check_description(line_num, segments[index_desc]),
        *check_auth(line_num, segments[index_auth]),
        *check_transport(line_num, segments[index_transport]),
        *check_install(line_num, segments[index_install]),
    ]


def check_entry(line_num: int, segments: List[str]) -> List[str]:

    raw_title = segments[index_title]
    description = segments[index_desc]
    auth = segments[index_auth]
    https = segments[index_https]
    cors = segments[index_cors]

    title_err_msgs = check_title(line_num, raw_title)
    desc_err_msgs = check_description(line_num, description)
    auth_err_msgs = check_auth(line_num, auth)
    https_err_msgs = check_https(line_num, https)
    cors_err_msgs = check_cors(line_num, cors)

    err_msgs = [
        *title_err_msgs,
        *desc_err_msgs,
        *auth_err_msgs,
        *https_err_msgs,
        *cors_err_msgs
    ]

    return err_msgs


def check_file_format(lines: List[str]) -> List[str]:

    err_msgs = []
    category_title_in_index = []
    mcp_lines = get_mcp_line_numbers(lines)

    alphabetical_err_msgs = check_alphabetical_order(lines)
    err_msgs.extend(alphabetical_err_msgs)

    num_in_category = min_entries_per_category + 1
    category = ''
    category_line = 0

    for line_num, line_content in enumerate(lines):

        category_title_match = category_title_in_index_re.match(line_content)
        if category_title_match:
            category_title_in_index.append(category_title_match.group(1))

        # check each category for the minimum number of entries
        if line_num not in mcp_lines and line_content.startswith(anchor):
            category_match = anchor_re.match(line_content)
            if category_match:
                if category_match.group(1) not in category_title_in_index:
                    err_msg = error_message(line_num, f'category header ({category_match.group(1)}) not added to Index section')
                    err_msgs.append(err_msg)
            else:
                err_msg = error_message(line_num, 'category header is not formatted correctly')
                err_msgs.append(err_msg)

            if num_in_category < min_entries_per_category:
                err_msg = error_message(category_line, f'{category} category does not have the minimum {min_entries_per_category} entries (only has {num_in_category})')
                err_msgs.append(err_msg)

            category = line_content.split(' ')[1]
            category_line = line_num
            num_in_category = 0
            continue

        # skips lines that we do not care about
        if not line_content.startswith('|') or (line_num not in mcp_lines and line_content.startswith('|---')):
            continue

        segments = line_content.split('|')[1:-1]
        is_mcp = line_num in mcp_lines
        if is_mcp:
            stripped_segments = [segment.strip() for segment in segments]
            if stripped_segments == mcp_header or (
                len(segments) == num_segments and
                all(re.fullmatch(r':?-{3,}:?', segment) for segment in stripped_segments)
            ):
                continue
            if len(segments) > num_segments:
                err_msgs.append(error_message(line_num, f'MCP entry must have exactly {num_segments} columns (have {len(segments)})'))
                continue
        else:
            num_in_category += 1
        if len(segments) < num_segments:
            err_msg = error_message(line_num, f'entry does not have all the required columns (have {len(segments)}, need {num_segments})')
            err_msgs.append(err_msg)
            continue
    
        for segment in segments:
            # every line segment should start and end with exactly 1 space
            if len(segment) - len(segment.lstrip()) != 1 or len(segment) - len(segment.rstrip()) != 1:
                err_msg = error_message(line_num, 'each segment must start and end with exactly 1 space')
                err_msgs.append(err_msg)
        
        segments = [segment.strip() for segment in segments]
        entry_err_msgs = check_mcp_entry(line_num, segments) if is_mcp else check_entry(line_num, segments)
        err_msgs.extend(entry_err_msgs)
    
    return err_msgs


def main(filename: str) -> None:

    with open(filename, mode='r', encoding='utf-8') as file:
        lines = list(line.rstrip() for line in file)

    file_format_err_msgs = check_file_format(lines)

    if file_format_err_msgs:
        for err_msg in file_format_err_msgs:
            print(err_msg)
        sys.exit(1)


if __name__ == '__main__':

    num_args = len(sys.argv)

    if num_args < 2:
        print('No .md file passed (file should contain Markdown table syntax)')
        sys.exit(1)

    filename = sys.argv[1]

    main(filename)
