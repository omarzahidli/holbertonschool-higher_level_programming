#!/usr/bin/python3

import urllib.request
import sys
url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    head = response.headers.get("X-Request-Id")
print(head)
