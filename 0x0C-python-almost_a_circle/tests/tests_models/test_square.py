#!/usr/bin/python3
"""
test Square class
"""
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import unittest
from io import StringIO
from contextlib import redirect_stdout


class TestSquareInstantiation(unittest.TestCase):
    """
    testing for instantioation of square class
    """
    def test_square_is_instance(self):
        self.assertIsInstance(Square(1, 2), Base)

    def test_square_is_instance1(self):
        self.assertIsInstance(Square(1, 2), Square)

    def test_square_is_subbase(self):
        self.assertEqual(issubclass(Square, Base), True)

    def test_square_is_subbase(self):
        self.assertEqual(issubclass(Square, Square), True)

    def test_id(self):
        Sqr1 = Square(10, 2, 0)
        Sqr2 = Square(10, 2)
        Sqr3 = Square(10, 0, 0, 12)
        Sqr4 = Square(10, 0, 0, 12)
        Sqr4.id = 15
        self.assertEqual(Sqr1.id + 1, Sqr2.id)
        self.assertEqual(Sqr3.id, 12)
        self.assertEqual(Sqr4.id, 15)

    def test_less_arguments(self):
        with self.assertRaises(TypeError):
            Sqr1 = Square()

    def test_more_arguments(self):
        with self.assertRaises(TypeError):
            Sqr2 = Square(10, 6, 5, 3, 7, 8)

    def test_getter_width(self):
        Sqr1 = Square(10, 2, 0, 0)
        self.assertEqual(Sqr1.width, 10)

    def test_getter_height(self):
        Sqr1 = Square(10, 2, 0, 0)
        self.assertEqual(Sqr1.height, 10)

    def test_getter_x(self):
        Sqr1 = Square(10, 2, 3, 7)
        self.assertEqual(Sqr1.x, 2)

    def test_getter_y(self):
        Sqr1 = Square(10, 2, 3, 7)
        self.assertEqual(Sqr1.y, 3)

    def test_getter_size(self):
        Sqr1 = Square(10, 2, 3, 7)
        self.assertEqual(Sqr1.size, 10)

    def test_setter_width(self):
        Sqr1 = Square(10, 2, 3, 7)
        Sqr1.width = 6
        self.assertEqual(Sqr1.width, 6)

    def test_setter_height(self):
        Sqr1 = Square(10, 2, 3, 7)
        Sqr1.height = 6
        self.assertEqual(Sqr1.height, 6)

    def test_setter_x(self):
        Sqr1 = Square(10, 2, 3, 7)
        Sqr1.x = 6
        self.assertEqual(Sqr1.x, 6)

    def test_setter_y(self):
        Sqr1 = Square(10, 2, 3, 7)
        Sqr1.y = 6
        self.assertEqual(Sqr1.y, 6)

    def test_setter_size(self):
        Sqr1 = Square(10, 2, 3, 7)
        Sqr1.size = 6
        self.assertEqual(Sqr1.size, 6)
        self.assertEqual(Sqr1.width, 6)
        self.assertEqual(Sqr1.height, 6)

    def test_privacy(self):
        Sqr = Square(10, 2)
        with self.assertRaises(AttributeError):
            Sqr.__width
        with self.assertRaises(AttributeError):
            Sqr.__height
        with self.assertRaises(AttributeError):
            Sqr.__x
        with self.assertRaises(AttributeError):
            Sqr.__y

    def test_passing_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(1.6, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 7.5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 10, 8.9)

    def test_passing_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("ahmed", 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "ahmed")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 10, "ahmed")

    def test_passing_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, True)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 10, True)

    def test_passing_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 8, 9], 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1, 8, 9])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 10, [1, 8, 9])

    def test_passing_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 8, 9), 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, (1, 8, 9))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 10, (1, 8, 9))

    def test_passing_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"name": "ahmed", "id": 7}, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"name": "ahmed", "id": 7})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 10, {"name": "ahmed", "id": 7})

    def test_width_equal_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 12)

    def test_width_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-17, 12)

    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(7, -8)

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(7, 8, -5)

    def test_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'), 8)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(7, float('inf'))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(7, 8, float('inf'))

    def test_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'), 8)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(7, float('nan'))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(7, 8, float('nan'))
