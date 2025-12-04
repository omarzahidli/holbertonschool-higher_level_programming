#!/usr/bin/python3
""" POST email """

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email as form data
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Make POST request
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as response:
        body = response.read()

    # Print response decoded in utf-8
    print(body.decode("utf-8"))
