#!/usr/bin/python3
"""
1-top_ten module
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot
    posts listed for a given subreddit. If the subreddit is invalid,
    prints None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python:top_ten.checker:v1.0 (by /u/example)"}
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )
    except requests.exceptions.RequestException:
        print(None)
        return

    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
    except ValueError:
        print(None)
        return

    if not posts:
        print(None)
        return

    for post in posts:
        print(post.get("data", {}).get("title"))
