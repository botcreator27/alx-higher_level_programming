#!/usr/bin/python3
""" class Base """


class BaseGeometry():
    """ class BaseGeometry with public instance method"""

    def area(self):
        """ function raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value
        Args:
        name(str): string
        value(int): value to be validated
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
