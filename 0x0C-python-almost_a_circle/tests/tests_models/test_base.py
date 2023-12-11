#!/usr/bin/python3
"""
test base class
"""
import unittest
from models.base import Base


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
