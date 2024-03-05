#!/usr/bin/python3
"""interview task"""
import requests
from sys import argv


if __name__ == "__main__":
    resp = requests.get(
        url="https://api.github.com/repos/{}/{}/commits".format(
            argv[2], argv[1]))
    if resp.status_code == 200:
        json_data = resp.json()
        for commit in json_data[:10]:
            print(commit.get('sha'), end=': ')
            print(commit.get('commit').get('author').get('name'))
