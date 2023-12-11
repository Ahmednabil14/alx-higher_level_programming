#!/usr/bin/python3
"""
square class
"""
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """
    square class that inherit from rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        square constructor
        arguments:
            size: the square side
            x: in horizontal
            y: in vertical
            id: the square id
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        informal string of the class
        """
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.width = self.height = value
        self.__size = value
