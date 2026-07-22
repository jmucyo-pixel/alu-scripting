#!/usr/bin/python3
"""Module that recursively counts keyword occurrences in hot article titles."""
import requests


def count_words(subreddit, word_list, counts={}, after=None):
    """Recursively count and print sorted keyword occurrences in hot titles."""
    if not counts:
        counts = {word.lower(): 0 for word in word_list}
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    headers = {"User-Agent": "linux:myredditapp:v1.0 (by /u/yourusername)"}
    params = {"after": after} if after else {}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=params)
    if response.status_code != 200:
        return
    data = response.json().get("data", {})
    posts = data.get("children", [])
    for post in posts:
        title = post.get("data", {}).get("title", "").lower().split()
        for word in title:
            if word in counts:
                counts[word] += 1
    after = data.get("after")
    if after is None:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print("{}: {}".format(word, count))
        return
    return count_words(subreddit, word_list, counts, after)
