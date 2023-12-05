#!/usr/bin/python3
"""
Write to file
"""


def write_file(filename="", text=""):
    """
    function that write to file
    arguments:
        filename: the file
        text: the text to add
    """
    with open(filename, "w", encoding='utf-8') as f:
        f.write(text)
        return len(text)
