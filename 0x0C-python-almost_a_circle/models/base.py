#!/usr/bin/python3
"""
Base class
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        static method that returns the JSON string
        representation of list_dictionaries
        arguments:
          list_dictionaries: list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
