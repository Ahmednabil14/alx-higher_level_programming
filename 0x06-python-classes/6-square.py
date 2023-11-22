#!/usr/bin/python3
"""
class Square that defines a square by: (based on 5-square.py)
"""


class Square:
    """

    class that define square
    attributes:
        size: the size of square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        create new instance from the class
        arguments:
            size:
                the size of square
            position:
                tuple of the position
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        getter function for size
        """
        return self.__size

    @property
    def position(self):
        """
        getter propert for position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter property for position
        """
        if not isinstance(value, tuple(int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        for x in range(self.__position[1]):
            print()
        for n in range(self.__size):
            for y in range(self.__position[0]):
                print(" ", end='')
            for i in range(self.__size):
                print("#", end='')
            print()
