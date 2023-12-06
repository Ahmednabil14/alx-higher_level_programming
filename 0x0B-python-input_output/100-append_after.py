#!/usr/bin/python3
"""
Search and update text file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a file,
    after each line containing a specific string
    """
    with open(filename, "r+") as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            if search_string in line:
                f.write(line)
                f.write(new_string)
            else:
                f.write(line)
