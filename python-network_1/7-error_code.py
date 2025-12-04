#!/usr/bin/python3
""" Error Code  """

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = requests.get(url)
        # This will raise an HTTPError for 4xx/5xx responses
        response.raise_for_status()
        print("Regular request")
    except requests.exceptions.HTTPError as e:
        # Print the actual HTTP status code
        print("Error code: {}".format(e.response.status_code))
