#!/usr/bin/python3
"""
How many subs?
"""
import requests


headers = {"User-Agent": "Chrome/125.0.0.0"}


def number_of_subscribers(subreddit):
    """Number of subs"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    r = requests.get(url, headers, allow_redirects=False)
    try:
        data = r.json()
        return data['data']['subscribers']
    except Exception:
        return 0
