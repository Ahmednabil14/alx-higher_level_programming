#!/usr/bin/python3
"""
program that show if object is instance from specific class or not
"""


def is_same_class(obj, a_class):
    """
    function that returns True if the object is exactly an
    instance of the specified class ; otherwise False.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
