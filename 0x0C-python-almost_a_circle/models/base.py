#!/usr/bin/python3
"""
Base class
"""


class Base:
    """
    the base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        the instantiantion method
        arguments:
            id: the id and it must be integer
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
