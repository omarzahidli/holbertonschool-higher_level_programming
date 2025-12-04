#!/usr/bin/python3
""" HTTPError """

import urllib.request
import sys

if __name__ = "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
    except urllib.error.HTTPError as e:
        print(f"Error: {e.code}")
