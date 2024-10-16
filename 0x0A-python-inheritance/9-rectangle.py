#!/usr/bin/python3
""" rectangle module nherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class"""
    def __init__(self, width, height):
        """ initialises rectangle attr as private"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ computes the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ returns the rectangle description """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
