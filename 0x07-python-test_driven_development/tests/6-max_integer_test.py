#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    class that tests max_integer function
    """
    def test_list1(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_list2(self):
        self.assertEqual(max_integer([9, 5, 11, 7]), 11)

    def test_none(self):
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        self.assertEqual(max_integer([3]), 3)

    def test_one_neg(self):
        self.assertEqual(max_integer([-10]), -10)

    def test_neg(self):
        self.assertEqual(max_integer([1, -2, -10, -5]), 1)

if __name__ == "__main__":
    unittest.main()
