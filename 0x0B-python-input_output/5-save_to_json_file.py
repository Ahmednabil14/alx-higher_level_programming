#!/usr/bin/python3
"""
Save Object to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file, using a JSON representation
    arguments:
        my_obj: the object to add to the json file
        filename: the json file
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
