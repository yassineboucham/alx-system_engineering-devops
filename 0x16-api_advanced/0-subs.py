#!/usr/bin/python3
"""
How many subs?
"""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    try:
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    except ValueError:
        # In case the response isn't JSON or can't be decoded
        return 0
