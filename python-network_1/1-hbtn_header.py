#!/usr/bin/python3

import urllib.request

url = input()
headers = { 'cfclearance': 'true' }
with urllib.request.urlopen(url) as response:
    body = response.read()
print(body.decode("utf-8").find("X-Request-Id"))
