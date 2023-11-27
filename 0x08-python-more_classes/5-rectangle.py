#!/usr/bin/python3
"""
class that define the rectangle
"""


class Rectangle:
    """
    class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
    """

    def __init__(self, width=0, height=0):
        """
        the construction
        """
        self.width = width
        self.height = height

    def __str__(self):
        """
        Instance method that returns an “informal” and nicely
        printable string representation of an instance
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        result = ""
        for i in range(self.__height):
            if i == self.__height - 1:
                result += "#" * self.__width
            else:
                result += "#" * self.__width + '\n'
        return result

    def __repr__(self):
        """
        should return a string representation of the rectangle to be
        able to recreate a new instance by using eval()
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        printing message when deleting instance
        """
        print("Bye rectangle...")

    @property
    def width(self):
        """
        getter prop for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        the setter for width attribute
        Exceptions:
            TypeError: if width is not int
            ValueError: if width < 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        Exceptions:
            TypeError: if height is not int
            ValueError: if height < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        function that calculate area of rectangle
        Return: the area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        function that calculate perimeter of rectangle
        Return: the perimeter
        if width or height == 0 return 0
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)
