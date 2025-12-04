#!/usr/bin/python3
""" POST email """

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = urllib.parse.urlencode(sys.argv[2])
    with urllib.request.urlopen(url) as repsonse:
        body = reasponse.read()
    print(body.decode("utf-8"))
