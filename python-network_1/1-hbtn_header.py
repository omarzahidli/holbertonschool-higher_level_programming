#!/usr/bin/python3
"""Fetches the X-Request-Id from the response header."""
import urllib.request
import sys
""" Import url from argv """
url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    """ Get header """
    head = response.headers.get("X-Request-Id")

print(head)
