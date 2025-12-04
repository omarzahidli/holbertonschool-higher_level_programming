#!/usr/bin/python3
"""Fetch posts from JSONPlaceholder and process them"""

import requests
import csv

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch all posts and print their titles"""
    try:
        response = requests.get(URL)
        print("Status Code: {}".format(response.status_code))
        if response.status_code == 200:
            posts = response.json()
            for post in posts:
                print(post.get("title"))
    except requests.exceptions.RequestException as e:
        print("Error fetching posts:", e)


def fetch_and_save_posts():
    """Fetch all posts and save them to posts.csv"""
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            posts = response.json()
            # Prepare list of dictionaries with only id, title, body
            simplified_posts = [
                {"id": post.get("id"), "title": post.get("title"), "body": post.get("body")}
                for post in posts
            ]
            # Write to CSV
            with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
                fieldnames = ["id", "title", "body"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(simplified_posts)
    except requests.exceptions.RequestException as e:
        print("Error fetching posts:", e)
