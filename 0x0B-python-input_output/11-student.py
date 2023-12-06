#!/usr/bin/python3
"""
Student to disk and reload
"""


class Student:
    """
    class that define students
    """
    def __init__(self, first_name, last_name, age):
        """
        instantiation method
        arguments:
            first_name: first name of student
            last_name: last name of student
            age: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        that retrieves a dictionary representation of a Student instance
        """
        dictionary = {}
        for attr in dir(self):
            if attr[0] == "_" and attr[1] == "_":
                continue
            x = getattr(self, attr)
            if not callable(x):
                if attrs is None:
                    dictionary.update({attr: x})
                else:
                    if attr in attrs:
                        dictionary.update({attr: x})
        return dictionary

    def reload_from_json(self, json):
        """
        function that replaces all attributes of the Student instance
        arguments:
            json: text like json file
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
