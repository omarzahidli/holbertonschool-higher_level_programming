#!/usr/bin/python3
""" Error Code  """


import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = requests.get(url)
        print(response.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(response.status_code))
