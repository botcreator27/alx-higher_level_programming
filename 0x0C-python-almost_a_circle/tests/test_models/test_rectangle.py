#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
""" test for class Rectangle"""


class Test_Rectangle(unittest.TestCase):
    """test cases for Rectangle behaviour"""
    def test_basic(self):
        """basic definition of Rectangle"""
        r1 = Rectangle(10, 2, 3, 4)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 1)

    def test_width(self):
        """tests for width: raises"""
        with self.assertRaises(TypeError):
            Rectangle("2", 5)

        with self.assertRaises(ValueError):
            Rectangle(0, 5)

    def test_invalid_height(self):
        """test height raises"""
        with self.assertRaises(TypeError):
            Rectangle(1, "22")

        with self.assertRaises(ValueError):
            Rectangle(5, -5)

    def test_invalid_attributes(self):
        """ tests attributes with invalid values"""
        with self.assertRaises(TypeError):
            Rectangle("3", (2), {2, 3}, "3")
        with self.assertRaises(ValueError):
            Rectangle(0, -2, -5, 0)

    def test_area(self):
        """ tests area method"""
        r1 = Rectangle(1, 6)
        self.assertEqual(r1.area(), 6)
