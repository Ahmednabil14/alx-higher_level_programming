#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
program for geometry
"""


class Square(Rectangle):
    """
    class square that inherit from rectangle
    """
    def __init__(self, size):
        """
        Instantiation with size
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
