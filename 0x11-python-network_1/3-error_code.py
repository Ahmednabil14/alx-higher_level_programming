#!/usr/bin/python3
"""Handling HTTP errors and displaying error codes."""
from urllib import request, error
from sys import argv


if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as resp:
            print(resp.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
