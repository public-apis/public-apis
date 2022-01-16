# -*- coding: utf-8 -*-

import re
from typing import List, Tuple, Dict


anchor = '###'
min_entries_per_section = 3
auth_keys = ['apiKey', 'OAuth', 'X-Mashape-Key', 'User-Agent', 'No']
punctuation = ['.', '?', '!']
https_keys = ['Yes', 'No']
cors_keys = ['Yes', 'No', 'Unknown']

index_title = 0
index_desc = 1
index_auth = 2
index_https = 3
index_cors = 4
index_link = 5
num_segments = 5

errors = []
title_links = []
anchor_re = re.compile(anchor + '\s(.+)')
section_title_re = re.compile('\*\s\[(.*)\]')
link_re = re.compile('\[(.+)\]\((http.*)\)')

# Type aliases
APIList = List[str]
Categories = Dict[str, APIList]
CategoriesLineNumber = Dict[str, int]


def error_message(line_number: int, message: str) -> str:
    line = line_number + 1
    return f'(L{line:03d}) {message}'


def get_categories_content(contents: List[str]) -> Tuple[Categories, CategoriesLineNumber]:

    categories = {}
    category_line_num = {}

    for line_num, line_content in enumerate(contents):

        if line_content.startswith(anchor):
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
                categories[category].append(title)

    return (categories, category_line_num)


def check_alphabetical_order(lines: List[str]) -> None:

    categories, category_line_num = get_categories_content(contents=lines)

    for category, api_list in categories.items():
        if sorted(api_list) != api_list:
            message = error_message(
                category_line_num[category], 
                f'{category} category is not alphabetical order'
            )
            errors.append(message)
