#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
from sys import argv


if __name__ == "__main__":
    header = {"Authorization": "Bearer {}".format(argv[2])}
    resp = requests.get(url="https://api.github.com/users/{}".format(
        argv[1]), headers=header)
    json_data = resp.json()
    print(json_data.get("id"))
