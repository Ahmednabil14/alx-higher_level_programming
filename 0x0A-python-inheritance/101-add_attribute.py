#!/usr/bin/python3
"""
Module that adds a new attribute to an object if it's possible
"""


def add_attribute(object, attribute, vlaue):
    """
     function that adds a new attribute to an object if it’s possible
    """
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attribute, vlaue)
