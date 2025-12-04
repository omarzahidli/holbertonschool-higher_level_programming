#!/usr/bin/python3
""" View Content """

import requests

url = "https://intranet.hbtn.io/status"

body = requests.get(url)

print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
