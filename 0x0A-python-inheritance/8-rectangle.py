#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
program for geometry
"""


class Rectangle(BaseGeometry):
    """
    Rectagle class that inherit from BaseGeometry class
    """
    def __init__(self, width, height):
        """
        Instantiation with width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
