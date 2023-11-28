#!/usr/bin/python3
"""
print the name
"""
def say_my_name(first_name, last_name=""):
    """
    function that print the name
    arguments:
        first_name: the first name
        last_name: the last name
    exceptions:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
