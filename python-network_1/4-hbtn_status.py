#!/usr/bin/python3
""" View Content """

import urllib.request

url = "https://intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    body = response.read()

print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
