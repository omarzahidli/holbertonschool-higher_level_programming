#!/usr/bin/python3
"""Module that fetches a URL using urllib with custom headers."""

import urllib.request


def fetch_status():
    """Fetch and print the status page with custom headers."""
    url = "https://intranet.hbtn.io/status"
    headers = {
        'cfclearance': 'true'
    }

    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as response:
        body = response.read()

    print(body.decode("utf-8"))


if __name__ == "__main__":
    fetch_status()
