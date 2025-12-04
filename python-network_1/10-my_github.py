#!/usr/bin/python3
"""Display GitHub user ID using Basic Authentication"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]  # Personal access token

    url = "https://api.github.com/user"

    try:
        response = requests.get(url, auth=(username, token))
        response.raise_for_status()
        user_data = response.json()
        print(user_data.get("id"))
    except requests.exceptions.RequestException:
        print("None")
