#!/usr/bin/python3
"""
Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    class that define rectangle
    inherit from Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class constructor
        arguments:
            width: rectangle's width
            height: rectangle's height
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.__x, self.__y, self.__width, self.__height)

    def validator(self, value, name):
        """
        function that chech if value is int
        arguments:
            value: the value to be checked
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

    @property
    def width(self):
        """
        getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter for width
        """
        self.validator(value, "width")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter for height
        """
        self.validator(value, "height")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter for x
        """
        self.validator(value, "x")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        getter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter for y
        """
        self.validator(value, "y")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        function that return rectangle area
        """
        return self.__width * self.__height

    def display(self):
        """
        function that prints in stdout the Rectangle instance
        with the character #
        """
        for y in range(self.__y):
            print()
        for h in range(self.__height):
            for x in range(self.__x):
                print(" ", end='')
            for w in range(self.__width):
                print("#", end='')
            print()

    def update(self, *args, **kwargs):
        """
        function that update rectangle instance attributes
            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute
        """
        if len(args) != 0:
            for i in range(len(args)):
                if i > 4:
                    break
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.__width = args[1]
                if i == 2:
                    self.__height = args[2]
                if i == 3:
                    self.__x = args[3]
                if i == 4:
                    self.__y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        function that return the class attributes as dictionary
        """
        dic = {}
        for attr in dir(self):
            if not callable(getattr(self, attr)) and attr[0] != '_':
                dic.update({attr:getattr(self, attr)})
        return dic
