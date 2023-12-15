#!/usr/bin/python3
"""
Base class
"""
import json
import os


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

    @staticmethod
    def from_json_string(json_string):
        """
        static method that returns the list of the
        JSON string representation json_string
        arguments:
            json_string: is a string representing a list of dictionaries
        """
        if not json_string or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        class method that returns an instance with all attributes already set
        arguments:
            dictionary: it is kwarg
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == 'Rectangle':
            r = Rectangle(1, 1)
            r.update(**dictionary)
            return r
        elif cls.__name__ == 'Square':
            s = Square(1)
            s.update(**dictionary)
            return s

    @classmethod
    def load_from_file(cls):
        """
        class method that returns a list of instances
        """
        list = []
        if not os.path.exists("{}.json".format(cls.__name__)):
            return []
        with open("{}.json".format(cls.__name__), 'r') as f:
            data = f.read()
        obj = cls.from_json_string(data)
        for dic in obj:
            list.append(cls.create(**dic))
        return list
