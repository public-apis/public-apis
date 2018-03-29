#!/usr/bin/env python3

import httplib2
import re
import socket
import sys


def parse_links(filename):
    """Returns a list of URLs from text file"""
    with open(filename) as fp:
        data = fp.read()
    raw_links = re.findall(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
        data)
    links = [raw_link.replace(')', '') for raw_link in raw_links]
    return links


def validate_links(links):
    """Checks each entry in JSON file for live link"""
    print('Validating {} links...'.format(len(links)))
    errors = []
    for link in links:
        h = httplib2.Http(disable_ssl_certificate_validation=True, timeout=5)
        try:
            resp = h.request(link, 'HEAD')
            code = int(resp[0]['status'])
            # check if status code is a client or server error
            if code >= 404:
                errors.append('{}: {}'.format(code, link))
        except TimeoutError:
            errors.append("TMO: " + link)
        except socket.error as socketerror:
            errors.append("SOC: {} : {}".format(socketerror, link))
    return errors


if __name__ == "__main__":
    num_args = len(sys.argv)
    if num_args < 2:
        print("No .md file passed")
        sys.exit(1)
    errors = validate_links(parse_links(sys.argv[1]))
    if len(errors) > 0:
        for err in errors:
            print(err)
        sys.exit(1)
