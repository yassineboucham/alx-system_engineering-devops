#!/usr/bin/python3
"""
How many subs?
"""
import requests


def number_of_subscribers(subreddit):
    """Number of subs"""
    headers = {"User-Agent": "My-User-Agent"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    r = requests.get(url, headers, allow_redirects=False)
    try:
        data = r.json().get("data").get("subscribers")
        return data
    except Exception:
        return 0
