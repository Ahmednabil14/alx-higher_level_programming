#!/usr/bin/python3
"""
program that show if a class inherit from another class
"""


def inherits_from(obj, a_class):
    """
    function that returns True if the object is an instance of
    a class that inherited (directly or indirectly) from
    the specified class ; otherwise False.
    """
    if type(obj) is not a_class:
        return isinstance(obj, a_class)
    return False
