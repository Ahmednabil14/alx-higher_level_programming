#!/usr/bin/python3
"""
program for geometry
"""
Rectangle = __import__('9-rectangle').Rectangle


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

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
