#!/usr/bin/python3
"""
class Square that defines a square by: (based on 3-square.py)
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
        self.__size = size

    @property
    def size(self):
        """
        getter function
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter function
        arguments:
            value: the setter value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        function that calculate the square area
        Return: the area
        """
        return self.__size * self.__size

    def my_print(self):
        """
        function  that prints in stdout the square with the character #
        Return: void
        """
        if self.__size == 0:
            print()
        for n in range(0, self.__size):
            for i in range(0, self.__size):
                print("#", end='')
            print()
