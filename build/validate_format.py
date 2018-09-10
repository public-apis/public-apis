#!/usr/bin/env python3

import re
import sys

anchor = '###'
min_entries_per_section = 3
auth_keys = ['apiKey', 'OAuth', 'X-Mashape-Key', 'No']
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
previous_links = []
anchor_re = re.compile(anchor + '\s(.+)')
section_title_re = re.compile('\*\s\[(.*)\]')
link_re = re.compile('\[(.+)\]\((http.*)\)')


def add_error(line_num, message):
    """adds an error to the dynamic error list"""
    err = '(L{:03d}) {}'.format(line_num + 1, message)
    errors.append(err)


def check_alphabetical(lines):
    """
    checks if all entries per section are in alphabetical order based in entry title
    """
    sections = {}
    section_line_num = {}
    for line_num, line in enumerate(lines):
        if line.startswith(anchor):
            category = line.split(anchor)[1].strip()
            sections[category] = []
            section_line_num[category] = line_num
            continue
        if not line.startswith('|') or line.startswith('|---'):
            continue
        raw_title = [x.strip() for x in line.split('|')[1:-1]][0]
        title_re_match = link_re.match(raw_title)
        if title_re_match:
            sections[category].append(title_re_match.group(1).upper())

    for category, entries in sections.items():
        if sorted(entries) != entries:
            add_error(section_line_num[category], "{} section is not in alphabetical order".format(category))


def check_entry(line_num, segments):
    # START Title
    raw_title = segments[index_title]
    title_re_match = link_re.match(raw_title)
    # url should be wrapped in '[TITLE](LINK)' Markdown syntax
    if not title_re_match:
        add_error(line_num, 'Title syntax should be "[TITLE](LINK)"')
    else:
        # do not allow "... API" in the entry title
        title = title_re_match.group(1)
        if title.upper().endswith(' API'):
            add_error(line_num, 'Title should not end with "... API". Every entry is an API here!')
        # do not allow duplicate links
        link = title_re_match.group(2)
        if link in previous_links:
            add_error(line_num, 'Duplicate link - entries should only be included in one section')
        else:
            previous_links.append(link)
    # END Title
    # START Description
    # first character should be capitalized
    char = segments[index_desc][0]
    if char.upper() != char:
        add_error(line_num, "first character of description is not capitalized")
    # last character should not punctuation
    char = segments[index_desc][-1]
    if char in punctuation:
        add_error(line_num, "description should not end with {}".format(char))
    desc_length = len(segments[index_desc])
    if desc_length > 100:
        add_error(line_num, "description should not exceed 100 characters (currently {})".format(desc_length))
    # END Description
    # START Auth
    # values should conform to valid options only
    auth = segments[index_auth]
    if auth != 'No' and (not auth.startswith('`') or not auth.endswith('`')):
        add_error(line_num, "auth value is not enclosed with `backticks`")
    if auth.replace('`', '') not in auth_keys:
        add_error(line_num, "{} is not a valid Auth option".format(auth))
    # END Auth
    # START HTTPS
    # values should conform to valid options only
    https = segments[index_https]
    if https not in https_keys:
        add_error(line_num, "{} is not a valid HTTPS option".format(https))
    # END HTTPS
    # START CORS
    # values should conform to valid options only
    cors = segments[index_cors]
    if cors not in cors_keys:
        add_error(line_num, "{} is not a valid CORS option".format(cors))
    # END CORS


def check_format(filename):
    """
    validates that each line is formatted correctly,
    appending to error list as needed
    """
    with open(filename) as fp:
        lines = list(line.rstrip() for line in fp)
    check_alphabetical(lines)
    # START Check Entries
    num_in_category = min_entries_per_section + 1
    category = ""
    category_line = 0
    for line_num, line in enumerate(lines):
        if section_title_re.match(line):
            title_links.append(section_title_re.match(line).group(1))
        # check each section for the minimum number of entries
        if line.startswith(anchor):
            match = anchor_re.match(line)
            if match:
                if match.group(1) not in title_links:
                    add_error(line_num, "section header ({}) not added as a title link".format(match.group(1)))
            else:
                add_error(line_num, "section header is not formatted correctly")
            if num_in_category < min_entries_per_section:
                add_error(category_line, "{} section does not have the minimum {} entries (only has {})".format(
                    category, min_entries_per_section, num_in_category))
            category = line.split(' ')[1]
            category_line = line_num
            num_in_category = 0
            continue
        # skips lines that we do not care about
        if not line.startswith('|') or line.startswith('|---'):
            continue
        num_in_category += 1
        segments = line.split('|')[1:-1]
        if len(segments) < num_segments:
            add_error(line_num, "entry does not have all the required sections (have {}, need {})".format(
                len(segments), num_segments))
            continue
        # START Global
        for segment in segments:
            # every line segment should start and end with exactly 1 space
            if len(segment) - len(segment.lstrip()) != 1 or len(segment) - len(segment.rstrip()) != 1:
                add_error(line_num, "each segment must start and end with exactly 1 space")
        # END Global
        segments = [seg.strip() for seg in segments]
        check_entry(line_num, segments)
    # END Check Entries


def main():
    if len(sys.argv) < 2:
        print("No file passed (file should contain Markdown table syntax)")
        sys.exit(1)
    check_format(sys.argv[1])
    if len(errors) > 0:
        for err in errors:
            print(err)
        sys.exit(1)


if __name__ == "__main__":
    main()
