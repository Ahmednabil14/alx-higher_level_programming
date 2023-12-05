#!/usr/bin/python3
"""
 Read file
"""


def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout
    """
    with open("my_file_0.txt", "r") as f:
        file = f.read()
        print(file)
