#!/usr/bin/python3
"""
class Square that defines a square by: (based on 1-square.py)
"""


class Square:
    """

    class that define square
    attributes:
        size: the size of square
    """
    def __init__(self, size=0):
        """
        create new instance from the class
        arguments:
            size:
                the size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
