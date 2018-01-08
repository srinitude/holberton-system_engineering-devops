#!/usr/bin/python3
"""
Returns a list of all the hot titles in a subreddit
"""
import requests


def recurse(subreddit, hot_list=[], fullname=""):
    """
    Returns a list of all the hot titles in a subreddit
    """
    if type(subreddit) is not str:
        return None
    base_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if len(fullname) > 0:
        base_url += "?after={}".format("fullname")
    headers = {'user-agent': 'safari:holberton/0.1.0 (by /u/srinitude)'}
    response = requests.get(base_url,
                            headers=headers)
    if response.status_code != 200:
        return None
    response = response.json()
    after = response.get("data").get("after")
    hot_posts = response.get("data").get("children")
    if len(hot_posts) == 0:
        return hot_list
    for post in hot_posts:
        title = post.get("data").get("title")
        hot_list.append(title)
    return recurse(subreddit, hot_list, after)
