#!/usr/bin/python3
"""
program for geometry
"""


class BaseGeometry:
    """
    BaseGeometry class
    """
    def area(self):
        """
        function that raising exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        function that validate value
        arguments:
            name: string value
            value: must be intger
        exceptions:
            TypeError: <name> must be an integer if value not int
            ValueError: <name> must be greater than 0 if value < 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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

    def __str__(self):
        """
        return string of informal way of object
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """
        function that return area of rectange
        """
        return self.__height * self.__width


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

    def area(self):
        """
        function that return area of square
        """
        return self.__size * self.__size
