#!/usr/bin/python3
""" this module defines class Square, Rectangle subclass"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class square """
    def __init__(self, size):
        """ initialises the private attr size
        Args:
            size: must be a positive int
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ revises how area computes """
        return self.__size ** 2
