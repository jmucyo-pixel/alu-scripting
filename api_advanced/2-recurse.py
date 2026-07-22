#!/usr/bin/python3
"""Module that recursively queries the Reddit API for all hot articles."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively return a list of titles of all hot articles."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    headers = {"User-Agent": "linux:myredditapp:v1.0 (by /u/yourusername)"}
    params = {"after": after} if after else {}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=params)
    if response.status_code != 200:
        return None
    data = response.json().get("data", {})
    posts = data.get("children", [])
    if not posts:
        return hot_list if hot_list else None
    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))
    after = data.get("after")
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
