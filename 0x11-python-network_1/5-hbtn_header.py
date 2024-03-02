#!/usr/bin/python3
"""displays the value of the variable X-Request-Id"""
import requests
from sys import argv


if __name__ == "__main__":
    resp = requests.get(url=argv[1])
    print(resp.headers["X-Request-Id"])
