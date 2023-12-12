#!/usr/bin/python3
"""
Base class
"""
import json
import csv


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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class method that writes the JSON string
        representation of list_objs to a file
        arguments:
            list_objs: is a list of instances who inherits of Base
        """
        dic_list = []
        if list_objs is not None:
            for i in list_objs:
                if isinstance(i, Base):
                    dic_list.append(i.to_dictionary())
        with open("{}.json".format(cls.__name__), 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(dic_list))
