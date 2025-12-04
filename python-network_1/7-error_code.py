#!/usr/bin/python3
"""Send a request to a URL and handle HTTP error codes"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = requests.get(url)
        # Check if the status code indicates an error
        if response.status_code >= 400:
            print("Error code: {}".format(response.status_code))
        else:
            print(response.text)
    except requests.exceptions.RequestException as e:
        status = e.response.status_code if e.response else "N/A"
        print("Error code: {}".format(status))
