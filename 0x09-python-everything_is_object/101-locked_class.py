#!/usr/bin/python3
"""
prevents the user from dynamically creating new instance attributes
"""


class LockedClass:
    """
    class that prevents the user from dynamically creating
    new instance attributes
    """
    __slots__ = ["first_name"]
