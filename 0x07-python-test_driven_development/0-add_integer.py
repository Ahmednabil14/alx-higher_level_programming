#!/usr/bin/python3
"""
adding two numbers
"""


def add_integer(a, b=98):
    """
    function that add two numbers
    argument:
        a: the first number
        b: the second number
    Return:
        the result
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
