#!/usr/bin/python3
"""Search for a user by sending a POST request with a letter"""

import requests
import sys

if __name__ == "__main__":
    # Get the letter from command-line argument, default to ""
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': letter}

    try:
        response = requests.post("http://0.0.0.0:5000/search_user", data=data)
        try:
            result = response.json()
            if result:
                print("[{}] {}".format(result.get("id"), result.get("name")))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
    except requests.exceptions.RequestException:
        print("No result")
