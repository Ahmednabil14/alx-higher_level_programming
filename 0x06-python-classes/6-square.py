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
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        getter function for size
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
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        else:
            for x in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size)
