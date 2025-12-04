#!/usr/bin/python3
"""Get url with headers"""


import urllib.request
url = "https://intranet.hbtn.io/status"
headers = {'cfclearance': 'true'}
req = urllib.request.Request(url, headers)
urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
with urllib.request.urlopen(req) as response:
    body = response.read()
