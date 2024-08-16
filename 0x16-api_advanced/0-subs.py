#!/usr/bin/python3
"""
How many subs?
"""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the response is successful
        if response.status_code == 200:
            data = response.json()
            # Safely access subscriber count
            return data.get('data', {}).get('subscribers', 0)
        
        # If the subreddit is invalid, Reddit returns 301 or 302
        return 0

    except requests.RequestException:
        # Catch any requests exceptions
        return 0
