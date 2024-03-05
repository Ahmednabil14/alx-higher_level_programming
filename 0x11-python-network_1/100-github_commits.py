#!/usr/bin/python3
"""interview task"""
import requests
from sys import argv


if __name__ == "__main__":
    i = 0
    resp = requests.get(
        url="https://api.github.com/repos/{}/{}/commits".format(
            argv[1], argv[2]))
    if resp.status_code == 200:
        json_data = resp.json()
        while i < 10:
            try:
                print("{}: {}".format(
                    json_data[i].get("sha"), json_data[i].get(
                        "commit").get("author").get("name")))
            except Exception:
                break
            i += 1
