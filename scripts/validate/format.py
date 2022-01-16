# -*- coding: utf-8 -*-

import re


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


def error_message(line_number: int, message: str) -> str:
    line = line_number + 1
    return f'(L{line:03d}) {message}'
