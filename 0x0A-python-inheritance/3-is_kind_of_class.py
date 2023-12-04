#!/usr/bin/python3
"""
program that show if the object is instance from class
"""


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    else:
        return False
