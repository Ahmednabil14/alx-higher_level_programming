#!/usr/bin/python3
"""sends a POST request"""
import requests
from sys import argv


if __name__ == "__main__":
    data = {"email": "{}".format(argv[2])}
    resp = requests.post(url=argv[1], data=data)
    print(resp.text)
