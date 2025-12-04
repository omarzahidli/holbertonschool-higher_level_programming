#!/usr/bin/python3
""" POST email """

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    data = urllib.parse.urlencode({'email': sys.argv[2]})
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as repsonse:
        body = reasponse.read()
    print(body.decode("utf-8"))
