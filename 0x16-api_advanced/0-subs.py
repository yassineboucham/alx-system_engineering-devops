#!/usr/bin/python3
"""
    returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """number_of_subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(url, allow_redirects=False)
    try:
        data = req.json()
        return data['data']['subscribers']
    except Exception:
        return 0
