#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first
10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts
    for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        "User-Agent": "python:api_advanced:v1.0 (by /u/reddit_api_project)"
    }

    params = {
        "limit": 10
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get("data").get("children")

    for post in posts:
        print(post.get("data").get("title"))
