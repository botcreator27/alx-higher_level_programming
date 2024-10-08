#!/usr/bin/python3
""" Unittest for max_integer([..]) """


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ test cases for max integer """

    def test_max(self):
        """ Test with list of integers"""
        data = [1, 2, 3, 4, 5]
        result = max_integer(data)
        self.assertEqual(result, 5)

    def test_char(self):
        """ Test with other data type """
        data = ['d', 'a', 'b', "c"]
        result = max_integer(data)
        self.assertEqual(result, 'd')

    def test_not_int(self):
        """ test with int and str types """
        data = [ 9, "hello", 'c', 10]
        self.assertRaises(TypeError, max_integer, data)

    def test_empty(self):
        """Test with an empty list: should return None"""
        data = []
        result = max_integer(data)
        self.assertEqual(result, None)

    def test_negative(self):
        """Test with negative values"""
        data = [-2, -6, -1, -9]
        result = max_integer(data)
        self.assertEqual(result, -1)

    def test_float(self):
        """Test with a list of mixed ints and floats"""
        data = [3, 5.5, 1]
        result = max_integer(data)
        self.assertEqual(result, 5.5)

    def test_not_list(self):
        """Test with a parameter that's not a list: raise TypeError"""
        self.assertRaises(TypeError, max_integer, 9)

    def test_unique(self):
        """Test with a list of one int: should return the value of this int"""
        data = [4]
        result = max_integer(data)
        self.assertEqual(result, 4)

    def test_same(self):
        """Test with a list of identical values"""
        data = [100, 100, 100]
        result = max_integer(data)
        self.assertEqual(result, 100)

    def test_none(self):
        """Test with a None as parameter: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, None)


if __name__ == '__main__':
    unittest.main()
