# -*- coding: utf-8 -*-

import re
import sys
from string import punctuation
from typing import List, Tuple, Dict, Optional

# Temporary replacement
# The descriptions that contain () at the end must adapt to the new policy later
punctuation = punctuation.replace('()', '')

anchor = '###'
auth_keys = ['apiKey', 'OAuth', 'X-Mashape-Key', 'User-Agent', 'No']
https_keys = ['Yes', 'No']
cors_keys = ['Yes', 'No', 'Unknown']
transport_keys = ['stdio', 'HTTP', 'SSE']

index_title = 0
index_desc = 1
index_auth = 2
index_https = 3
index_cors = 4

num_segments = 5
min_entries_per_category = 3
max_description_length = 100

# Install column uses an en dash when a server is not listed on a marketplace.
en_dash = '\u2013'
install_separator = '\u00b7'

# REST API entries and MCP server entries share a five-column Markdown table but
# they carry different values in the last two columns. The column kind is decided
# by the table header so a Transport or Install value is never read as HTTPS/CORS.
rest_table = 'rest'
mcp_table = 'mcp'
sponsored_table = 'sponsored'

rest_header = ['API', 'Description', 'Auth', 'HTTPS', 'CORS']
mcp_header = ['Name', 'Description', 'Auth', 'Transport', 'Install']
sponsored_header = ['API', 'Description', 'Call this API']

anchor_re = re.compile(anchor + r'\s(.+)')
category_title_in_index_re = re.compile(r'\*\s\[(.*)\]')
link_re = re.compile(r'\[(.+)\]\((http.*)\)')
# Markdown alignment row: every cell is an optional colon, at least three
# hyphens and an optional colon, e.g. |---|:---| or | --- | :---: |.
separator_re = re.compile(r'^\|(?:\s*:?-{3,}:?\s*\|)+$')

# Type aliases
APIList = List[str]
Categories = Dict[str, APIList]
CategoriesLineNumber = Dict[str, int]


def error_message(line_number: int, message: str) -> str:
    line = line_number + 1
    return f'(L{line:03d}) {message}'


def get_table_cells(line: str) -> List[str]:
    return [cell.strip() for cell in line.split('|')[1:-1]]


def is_separator_row(line: str) -> bool:
    return bool(separator_re.match(line))


def get_header_table_kind(line: str) -> Optional[str]:
    cells = get_table_cells(line)
    if cells == rest_header or cells == rest_header + ["Call this API"]:
        return rest_table
    if cells == mcp_header:
        return mcp_table
    if cells == sponsored_header:
        return sponsored_table
    return None


def get_categories_content(contents: List[str], include_mcp: bool = False) -> Tuple[Categories, CategoriesLineNumber]:

    categories = {}
    category_line_num = {}

    category = None
    table_kind = rest_table
    indexed_categories = {match.group(1) for line in contents
                          if (match := category_title_in_index_re.match(line))}

    for line_num, line_content in enumerate(contents):

        if line_content.startswith(anchor):
            category = line_content.split(anchor)[1].strip()
            categories[category] = []
            category_line_num[category] = line_num
            table_kind = rest_table
            continue

        if include_mcp and line_content.strip() == "## MCP Servers":
            category = "MCP Servers"
            categories[category] = []
            category_line_num[category] = line_num
            table_kind = mcp_table
            continue

        # A top-level heading (including "## MCP Servers") leaves the previous
        # REST category, so its table rows are not attributed to it.
        if line_content.startswith('#'):
            category = None
            table_kind = rest_table
            continue

        if not line_content.startswith('|'):
            table_kind = rest_table
            continue

        if is_separator_row(line_content):
            continue

        header_kind = get_header_table_kind(line_content)
        if header_kind is not None and not (
                category in indexed_categories and header_kind != rest_table):
            table_kind = header_kind
            continue

        if (table_kind != rest_table and not (include_mcp and table_kind == mcp_table)) or category is None:
            continue

        cells = get_table_cells(line_content)
        if not cells:
            continue

        title_match = link_re.match(cells[0])
        if title_match:
            categories[category].append(title_match.group(1).upper())

    return (categories, category_line_num)


def check_alphabetical_order(lines: List[str]) -> List[str]:

    err_msgs = []

    categories, category_line_num = get_categories_content(contents=lines, include_mcp=True)

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

    if not description:
        err_msg = error_message(line_num, 'description should not be empty')
        err_msgs.append(err_msg)
        return err_msgs

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

    err_msgs = []

    backtick = '`'
    # Comma-separate the transports a server supports, each in backticks.
    options = [option.strip() for option in transport.split(',')]
    for option in options:
        if (not option.startswith(backtick) or not option.endswith(backtick)
                or option.replace(backtick, '') not in transport_keys):
            err_msg = error_message(line_num, f'{transport} is not a valid Transport option')
            err_msgs.append(err_msg)
            break

    return err_msgs


def check_install(line_num: int, install: str) -> List[str]:

    err_msgs = []

    if install == en_dash:
        return err_msgs

    listings = [listing.strip() for listing in install.split(install_separator)]
    if not listings or any(not link_re.fullmatch(listing) for listing in listings):
        err_msg = error_message(line_num, f'{install} is not a valid Install option')
        err_msgs.append(err_msg)

    return err_msgs


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


def check_mcp_entry(line_num: int, segments: List[str]) -> List[str]:

    raw_name = segments[index_title]
    description = segments[index_desc]
    auth = segments[index_auth]
    transport = segments[index_https]
    install = segments[index_cors]

    title_err_msgs = check_title(line_num, raw_name)
    desc_err_msgs = check_description(line_num, description)
    auth_err_msgs = check_auth(line_num, auth)
    transport_err_msgs = check_transport(line_num, transport)
    install_err_msgs = check_install(line_num, install)

    err_msgs = [
        *title_err_msgs,
        *desc_err_msgs,
        *auth_err_msgs,
        *transport_err_msgs,
        *install_err_msgs
    ]

    return err_msgs


def check_segments(line_num: int, segments: List[str], required_segments: int) -> List[str]:

    err_msgs = []

    if len(segments) < required_segments:
        err_msg = error_message(line_num, f'entry does not have all the required columns (have {len(segments)}, need {required_segments})')
        err_msgs.append(err_msg)
        return err_msgs

    for segment in segments:
        # every line segment should start and end with exactly 1 space
        if len(segment) - len(segment.lstrip()) != 1 or len(segment) - len(segment.rstrip()) != 1:
            err_msg = error_message(line_num, 'each segment must start and end with exactly 1 space')
            err_msgs.append(err_msg)

    return err_msgs


def check_file_format(lines: List[str]) -> List[str]:

    err_msgs = []
    category_title_in_index = []

    alphabetical_err_msgs = check_alphabetical_order(lines)
    err_msgs.extend(alphabetical_err_msgs)

    # Only sections that actually carry REST rows are API categories. Heading
    # sections such as the sponsored preface or the MCP server list are not
    # indexed categories and must not be checked for minimum entries or Index
    # membership.
    categories, _ = get_categories_content(contents=lines)
    rest_categories = {name for name, api_list in categories.items() if api_list}
    rest_categories.update(match.group(1) for line in lines
                           if (match := category_title_in_index_re.match(line)))
    # Indexed categories remain REST categories even when they have no rows.
    if "## Index" in lines:
        rest_categories.update(line.split(anchor)[1].strip()
                               for line in lines[lines.index("## Index") + 1:]
                               if line.startswith(anchor))

    num_in_category = min_entries_per_category + 1
    category = ''
    category_line = 0
    category_is_rest = False
    table_kind = rest_table

    for line_num, line_content in enumerate(lines):

        category_title_match = category_title_in_index_re.match(line_content)
        if category_title_match:
            category_title_in_index.append(category_title_match.group(1))

        # check each category for the minimum number of entries
        if line_content.startswith(anchor):
            heading = line_content.split(anchor)[1].strip()
            is_rest_category = heading in rest_categories

            if is_rest_category:
                category_match = anchor_re.match(line_content)
                if category_match:
                    if category_match.group(1) not in category_title_in_index:
                        err_msg = error_message(line_num, f'category header ({category_match.group(1)}) not added to Index section')
                        err_msgs.append(err_msg)
                else:
                    err_msg = error_message(line_num, 'category header is not formatted correctly')
                    err_msgs.append(err_msg)

            if category_is_rest and num_in_category < min_entries_per_category:
                err_msg = error_message(category_line, f'{category} category does not have the minimum {min_entries_per_category} entries (only has {num_in_category})')
                err_msgs.append(err_msg)

            category = line_content.split(' ')[1]
            category_line = line_num
            category_is_rest = is_rest_category
            num_in_category = 0
            table_kind = rest_table
            continue

        # A top-level heading ends the previous category without starting a new one.
        if line_content.startswith('#'):
            if category_is_rest and num_in_category < min_entries_per_category:
                err_msg = error_message(category_line, f'{category} category does not have the minimum {min_entries_per_category} entries (only has {num_in_category})')
                err_msgs.append(err_msg)
            category_is_rest = False
            table_kind = rest_table
            continue

        # skips lines that we do not care about
        if not line_content.startswith('|'):
            table_kind = rest_table
            continue

        # Markdown alignment rows are table chrome, not entries.
        if is_separator_row(line_content):
            continue

        header_kind = get_header_table_kind(line_content)
        if header_kind is not None and not (
                category_is_rest and header_kind != rest_table):
            table_kind = header_kind
            continue

        if table_kind == sponsored_table:
            continue

        num_in_category += 1
        segments = line_content.split('|')[1:-1]

        if table_kind == mcp_table:
            segment_err_msgs = check_segments(line_num, segments, num_segments)
            err_msgs.extend(segment_err_msgs)
            if segment_err_msgs and len(segments) < num_segments:
                continue
            segments = [segment.strip() for segment in segments]
            entry_err_msgs = check_mcp_entry(line_num, segments)
            err_msgs.extend(entry_err_msgs)
            continue

        segment_err_msgs = check_segments(line_num, segments, num_segments)
        err_msgs.extend(segment_err_msgs)
        if segment_err_msgs and len(segments) < num_segments:
            continue
        segments = [segment.strip() for segment in segments]
        entry_err_msgs = check_entry(line_num, segments)
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
