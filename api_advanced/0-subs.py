#!/usr/bin/python3
"""
0-subs module
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit. If an invalid subreddit is given,
    returns 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "python:subs.checker:v1.0 (by /u/example)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
    except requests.exceptions.RequestException:
        return 0

    if response.status_code != 200:
        return 0

    try:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    except ValueError:
        return 0
