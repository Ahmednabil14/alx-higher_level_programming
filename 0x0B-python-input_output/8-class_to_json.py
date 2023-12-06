#!/usr/bin/python3
"""
Class to JSON
"""


def class_to_json(obj):
    """
    function that returns the dictionary description with
    simple data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    """
    dictionary = {}
    for attr in dir(obj):
        if attr[0] == "_" and attr[1] == "_":
            continue
        x = getattr(obj, attr)
        if not callable(x):
            dictionary.update({attr: x})
    return dictionary
