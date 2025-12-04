#!/usr/bin/python3
""" View Content """

import requests

url = "https://intranet.hbtn.io/status"

body = requests.get(url)

print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
