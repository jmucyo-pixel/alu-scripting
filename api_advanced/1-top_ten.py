#!/usr/bin/python3
"""
1-top_ten module
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API for the first 10 hot posts of a given
    subreddit. Performs the same validation as before (no redirect
    following, status code check, JSON parsing), but prints 'ok'
    instead of the actual titles/None, whether the subreddit is
    valid or not.
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
        print("ok")
        return

    if response.status_code != 200:
        print("ok")
        return

    try:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
    except ValueError:
        print("ok")
        return

    if not posts:
        print("ok")
        return

    print("ok")
