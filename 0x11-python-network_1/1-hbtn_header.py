#!/usr/bin/python3
"""Extracting a specific header value from a response."""
from urllib import request
from sys import argv


if __name__ == "__main__":
    """main function"""
    with request.urlopen("{}".format(argv[1])) as resp:
        print(resp.headers.get("X-Request-Id"))
