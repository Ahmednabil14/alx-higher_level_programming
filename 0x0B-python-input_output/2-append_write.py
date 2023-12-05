#!/usr/bin/python3
"""
Append to a file
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    arguments:
        filename: the file
        text: the text to add
    """
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
        return len(text)
