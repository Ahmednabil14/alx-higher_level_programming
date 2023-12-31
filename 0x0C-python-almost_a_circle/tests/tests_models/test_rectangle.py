#!/usr/bin/python3
"""
test rectangle class
"""
from models.rectangle import Rectangle
from models.base import Base
import unittest
from io import StringIO
from contextlib import redirect_stdout


class TestRectangleInstantiation(unittest.TestCase):
    def test_rectangle_is_instance(self):
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_rectangle_is_subbase(self):
        self.assertEqual(issubclass(Rectangle, Base), True)

    def test_id(self):
        rec1 = Rectangle(10, 2, 0, 0)
        rec2 = Rectangle(10, 2)
        rec3 = Rectangle(10, 2, 0, 0, 12)
        rec4 = Rectangle(10, 2, 0, 0, 12)
        rec4.id = 15
        self.assertEqual(rec1.id + 1, rec2.id)
        self.assertEqual(rec3.id, 12)
        self.assertEqual(rec4.id, 15)

    def test_less_arguments(self):
        with self.assertRaises(TypeError):
            rec1 = Rectangle()
        with self.assertRaises(TypeError):
            rec2 = Rectangle(10)

    def test_more_arguments(self):
        with self.assertRaises(TypeError):
            rec2 = Rectangle(10, 6, 5, 3, 7, 8)

    def test_getter_width(self):
        rec1 = Rectangle(10, 2, 0, 0)
        self.assertEqual(rec1.width, 10)

    def test_getter_height(self):
        rec1 = Rectangle(10, 2, 0, 0)
        self.assertEqual(rec1.height, 2)

    def test_getter_x(self):
        rec1 = Rectangle(10, 2, 3, 7)
        self.assertEqual(rec1.x, 3)

    def test_getter_y(self):
        rec1 = Rectangle(10, 2, 3, 7)
        self.assertEqual(rec1.y, 7)

    def test_setter_width(self):
        rec1 = Rectangle(10, 2, 3, 7)
        rec1.width = 6
        self.assertEqual(rec1.width, 6)

    def test_setter_height(self):
        rec1 = Rectangle(10, 2, 3, 7)
        rec1.height = 6
        self.assertEqual(rec1.height, 6)

    def test_setter_x(self):
        rec1 = Rectangle(10, 2, 3, 7)
        rec1.x = 6
        self.assertEqual(rec1.x, 6)

    def test_setter_y(self):
        rec1 = Rectangle(10, 2, 3, 7)
        rec1.y = 6
        self.assertEqual(rec1.y, 6)

    def test_privacy(self):
        rec = Rectangle(10, 2)
        with self.assertRaises(AttributeError):
            rec.__width
        with self.assertRaises(AttributeError):
            rec.__height
        with self.assertRaises(AttributeError):
            rec.__x
        with self.assertRaises(AttributeError):
            rec.__y

    def test_passing_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1.6, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 5.8)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 10, 7.5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 10, 7, 8.9)

    def test_passing_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("ahmed", 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "ahmed")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 10, "ahmed")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 10, 7, "ahmed")

    def test_passing_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, True)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 10, True)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 10, 7, True)

    def test_passing_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 8, 9], 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 8, 9])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 10, [1, 8, 9])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 10, 7, [1, 8, 9])

    def test_passing_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 8, 9), 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 8, 9))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 10, (1, 8, 9))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 10, 7, (1, 8, 9))

    def test_passing_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"name": "ahmed", "id": 7}, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"name": "ahmed", "id": 7})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 10, {"name": "ahmed", "id": 7})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 10, 7, {"name": "ahmed", "id": 7})

    def test_width_equal_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 12)

    def test_width_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-17, 12)

    def test_height_equal_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(9, 0)

    def test_height_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(17, -12)

    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(7, 8, -8)

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(7, 8, 9, -5)

    def test_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 8)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, float('inf'))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 8, float('inf'))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 8, 8, float('inf'))

    def test_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 8)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, float('nan'))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 8, float('nan'))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 8, 8, float('nan'))


class TestRectangleArea(unittest.TestCase):
    def test_area1(self):
        r = Rectangle(2, 5)
        self.assertEqual(r.area(), 10)

    def test_area2(self):
        r = Rectangle(2, 5, 7, 9, 87)
        self.assertEqual(r.area(), 10)


class TestRectangleDisplay(unittest.TestCase):
    def test_display_width_height(self):
        r = Rectangle(2, 5)
        actual_result = "##\n"*5
        f = StringIO()
        with redirect_stdout(f):
            r.display()
        self.assertEqual(f.getvalue(), actual_result)

    def test_display_width_height_x(self):
        r = Rectangle(2, 5, 2)
        actual_result = "  ##\n"*5
        f = StringIO()
        with redirect_stdout(f):
            r.display()
        self.assertEqual(f.getvalue(), actual_result)

    def test_display_width_height_x_y(self):
        r = Rectangle(2, 5, 2, 4)
        actual_result = "\n"*4 + "  ##\n"*5
        f = StringIO()
        with redirect_stdout(f):
            r.display()
        self.assertEqual(f.getvalue(), actual_result)

    def test_display_width_height_y(self):
        r = Rectangle(2, 5, 0, 4)
        actual_result = "\n"*4 + "##\n"*5
        f = StringIO()
        with redirect_stdout(f):
            r.display()
        self.assertEqual(f.getvalue(), actual_result)


class TestRecrangleStr(unittest.TestCase):
    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        actual_result = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r), actual_result)

        r1 = Rectangle(5, 5, 1)
        r2 = Rectangle(5, 5, 1)
        actual_result = "[Rectangle] ({}) 1/0 - 5/5".format(r1.id + 1)
        self.assertEqual(str(r2), actual_result)

        r1 = Rectangle(5, 5)
        r2 = Rectangle(5, 5)
        actual_result = "[Rectangle] ({}) 0/0 - 5/5".format(r1.id + 1)
        self.assertEqual(str(r2), actual_result)


class TestRectangleUpdate(unittest.TestCase):
    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r1))
        r1.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r1))
        r1.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r1))
        r1.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r1))
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r1))
        r1.id = 885
        r1.update(5)
        self.assertEqual("[Rectangle] (5) 4/5 - 2/3", str(r1))
        r1.update(89, 6, x=8)
        self.assertEqual("[Rectangle] (89) 4/5 - 6/3", str(r1))
        r1.update(89, 6, id=8)
        self.assertEqual("[Rectangle] (89) 4/5 - 6/3", str(r1))
        r1.update(height=1)
        self.assertEqual("[Rectangle] (89) 4/5 - 6/1", str(r1))
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual("[Rectangle] (89) 3/1 - 2/1", str(r1))
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r1))

    def test_update_empty(self):
        r1 = Rectangle(10, 10, 10, 10, 89)
        r1.update()
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r1))

    def test_more_args(self):
        r1 = Rectangle(10, 10, 10, 10, 89)
        r1.update(5, 4, 2, 8, 9, 2, 7)
        self.assertEqual("[Rectangle] (5) 8/9 - 4/2", str(r1))

    def test_wrong_key(self):
        r1 = Rectangle(10, 10, 10, 10, 89)
        r1.update(ahmed=8)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r1))
        r1.update(ahmed=8, id=100)
        self.assertEqual("[Rectangle] (100) 10/10 - 10/10", str(r1))


class TestRectangleToDictionary(unittest.TestCase):
    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9, 1)
        dic = r1.to_dictionary()
        expected = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(expected, dic)
        self.assertEqual(type(dic), dict)
