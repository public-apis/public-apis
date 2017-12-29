#!/usr/bin/env python3

import json
import string
import sys

anchor = '###'
auth_keys = ['apiKey', 'OAuth', 'X-Mashape-Key', 'No']
punctuation = ['.', '?', '!']
https_keys = ['Yes', 'No']

index_title = 0
index_desc = 1
index_auth = 2
index_https = 3
index_link = 4

errors = []


def add_error(line_num, message):
    """adds an error to the dynamic error list"""
    err = '(L{:03d}) {}'.format(line_num+1, message)
    errors.append(err)


def check_format(filename):
    """
    validates that each line is formatted correctly,
    appending to error list as needed
    """
    with open(filename) as fp:
        lines = list(line.rstrip() for line in fp)

    # START Alphabetical Order
    category = ""
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
        title = [x.strip() for x in line.split('|')[1:-1]][0].upper()
        sections[category].append(title)

    for category, entries in sections.items():
        if sorted(entries) != entries:
            add_error(section_line_num[category], '{} section is not in alphabetical order'.format(category))
    # END Alphabetical Order

    # START Check Entries
    for line_num, line in enumerate(lines):
        if not line.startswith('|') or line.startswith('|---'):
            continue
        segments = line.split('|')[1:-1]
        # START Global
        for segment in segments:
            # every line segment should start and end with exactly 1 space
            if len(segment) - len(segment.lstrip()) != 1 or len(segment) - len(segment.rstrip()) != 1:
                add_error(line_num, "each segment must start and end with exactly 1 space")
        # END Global
        segments = [seg.strip() for seg in segments]
        # START Description
        # first character should be capitalized
        char = segments[index_desc][0]
        if char.upper() != char:
            add_error(line_num, "first char of Description is not capitalized")
        # last character should not punctuation
        char = segments[index_desc][-1]
        if char in punctuation:
            add_error(line_num, "description should not end with {}".format(char))
        # END Description
        # START Auth
        # values should conform to valid options only
        auth = segments[index_auth].replace('`', '')
        if auth not in auth_keys:
            add_error(line_num, "{} is not a valid Auth option".format(auth))
        # END Auth
        # START HTTPS
        # values should conform to valid options only
        https = segments[index_https]
        if https not in https_keys:
            add_error(line_num, "{} is not a valid HTTPS option".format(https))
        # END HTTPS
        # START Link
        # url should be wrapped in '[Go!]()' Markdown syntax
        link = segments[index_link]
        if not link.startswith('[Go!](http') or not link.endswith(')'):
            add_error(line_num, 'link format should be "[Go!](LINK)"')
        # END Link
    # END Check Entries

def main():
    num_args = len(sys.argv)
    if num_args < 2:
        print("No .md file passed")
        sys.exit(1)

    check_format(sys.argv[1])
    if len(errors) > 0:
        for err in errors:
            print(err)
        sys.exit(1)


if __name__ == "__main__":
    main()
