#!/usr/bin/python3
"""Sending a POST request with an email parameter."""
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    data = {"email": "{}".format(argv[2])}
    encode_data = parse.urlencode(data).encode()
    with request.urlopen(argv[1], data=encode_data) as resp:
        print(resp.read().decode("utf-8"))
