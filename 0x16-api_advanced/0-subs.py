#!/usr/bin/python3
"""Module for task 0"""

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit."""
    user_agent = "MyRedditBot/1.0"  # Modify this with your project information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    headers = {"User-Agent": user_agent}

    sub_info = requests.get(url, headers=headers, allow_redirects=False)
    
    if sub_info.status_code == 404:
        return 0
    elif sub_info.status_code >= 300:
        # Handle other error cases if needed
        return 0

    return sub_info.json().get("data").get("subscribers")

