#!/usr/bin/python3
""" Test for base.py """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test Base class behavior """

    def setUp(self):
        """ Reset nb_objects attribute before each test """
        Base._Base__nb_objects = 0

    def test_explicit_id(self):
        """ Test for when id is specified """
        b1 = Base(100)
        self.assertEqual(b1.id, 100)

        b2 = Base(50)
        self.assertEqual(b2.id, 50)

    def test_id_none(self):
        """ Test for when id is not specified: id should be auto-assigned """
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_mixedup_id(self):
        """ Test when instances may or may not have id provided """
        b1 = Base(100)
        b2 = Base()
        b3 = Base(50)
        b4 = Base()

        self.assertEqual(b1.id, 100)
        self.assertEqual(b2.id, 1)
        self.assertEqual(b3.id, 50)
        self.assertEqual(b4.id, 2)

    def test_increment(self):
        """ Test that auto-assigned ids increment consecutively """
        new_b1 = Base()
        new_b2 = Base(5)
        new_b3 = Base()

        self.assertEqual(new_b1.id + 1, new_b3.id)

    def test_privacy(self):
        """ Test that __nb_objects cannot be accessed directly """
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

if __name__ == "__main__":
    unittest.main()
