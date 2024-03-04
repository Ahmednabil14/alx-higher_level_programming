#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        data = {"q": argv[1]}
    else:
        data = {"q": ""}
    resp = requests.post(url="http://0.0.0.0:5000/search_user", data=data)
    if resp.status_code == 200:
        try:
            json = resp.json()
            if json:
                print("[{}] {}".format(json["id"], json["name"]))
            else:
                print("No result")
        except requests.exceptions.JSONDecodeError:
            print("Not a valid JSON")
