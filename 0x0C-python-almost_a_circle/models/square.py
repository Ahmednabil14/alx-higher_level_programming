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
        """
        getter for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter for size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        function that update square instance attributes
            1st argument should be the id attribute
            2nd argument should be the size attribute
            3th argument should be the x attribute
            4th argument should be the y attribute
        """
        if len(args) != 0:
            for i in range(len(args)):
                if i > 3:
                    break
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.size = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        function that return the class attributes as dictionary
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
