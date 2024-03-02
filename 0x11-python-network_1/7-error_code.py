#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response."""
import requests
from sys import argv


if __name__ == "__main__":
    resp = requests.get(argv[1])
    if resp.status_code == 200:
        print(resp.text)
    else:
        print("Error code: {}".format(resp.status_code))
