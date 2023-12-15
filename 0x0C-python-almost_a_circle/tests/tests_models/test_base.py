#!/usr/bin/python3
"""
test base class
"""
import unittest
import os
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):
    def test_none(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_not_none(self):
        b1 = Base(12)
        b2 = Base(88)
        self.assertEqual(b1.id, 12)
        self.assertEqual(b2.id, 88)

    def test_mix(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b2.id, b1.id + 1)
        self.assertEqual(b3.id, b1.id + 2)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, b1.id + 3)

    def test_calling_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_objects)

    def test_id(self):
        b = Base(345)
        b.id = 12
        self.assertEqual(b.id, 12)

    def test_two_constructor_arguments(self):
        with self.assertRaises(TypeError):
            b = Base(1, 2)


class TestBaseToJsonString(unittest.TestCase):
    def test_happy_case(self):
        dictionary = {'x': 2}
        result = Base.to_json_string([dictionary])
        expected_result = '[{"x": 2}]'
        self.assertEqual(result, expected_result)
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(type(result), str)

    def test_empty(self):
        dic = {}
        dic2 = [{}, {}]
        result = Base.to_json_string(dic)
        self.assertEqual(result, '[]')
        self.assertEqual(Base.to_json_string(dic2), '[{}, {}]')

    def test_None(self):
        dic = None
        result = Base.to_json_string(dic)
        self.assertEqual(result, '[]')


class TestSaveToFile(unittest.TestCase):

    def test_none_rectangle(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(f.read(), '[]')
        os.remove("Rectangle.json")

    def test_empty_rectangle(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(f.read(), '[]')
        os.remove("Rectangle.json")

    def test_none_square(self):
        Square.save_to_file(None)
        with open("Square.json", 'r') as f:
            self.assertEqual(f.read(), '[]')
        os.remove("Square.json")

    def test_empty_square(self):
        Square.save_to_file([])
        with open("Square.json", 'r') as f:
            self.assertEqual(f.read(), '[]')
        os.remove("Square.json")

    def test__square(self):
        Square.save_to_file([Square(1, 2, 3, 4)])
        with open("Square.json", 'r') as f:
            self.assertEqual(len(f.read()), 38)
        os.remove("Square.json")


class TestFromJsonString(unittest.TestCase):
    def test_happy_case(self):
        list_input = [
            {'id': 89},
            {'id': 7}
        ]
        list_output = Base.to_json_string(list_input)
        list_json = Base.from_json_string(list_output)
        self.assertEqual(type(list_json), list)
        self.assertEqual(list_input, list_json)

    def test_empty(self):
        out = Rectangle.from_json_string('')
        self.assertEqual([], out)

    def test_none(self):
        out = Square.from_json_string('')
        self.assertEqual(out, [])


class TestCreat(unittest.TestCase):
    def test_happy_case(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))

    def test_dictinary(self):
        r1 = Rectangle.create(**{'width': 2, 'height': 3, 'x': 12,
                                 'y': 5, 'id': 6})
        self.assertEqual(str(r1), '[Rectangle] (6) 12/5 - 2/3')

    def test_square(self):
        s1 = Square(1)
        s = Square.create(**{'size': 2})
        self.assertEqual(str(s), "[Square] ({}) 0/0 - 2".format(s1.id + 1))


class TestLoadFromFile(unittest.TestCase):
    def test1(self):
        pass