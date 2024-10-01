#!/usr/bin/python3
""" Defines a class Square"""


class Square:
        """
        Initialising class Square with private attribute

        Attributes:
           size: holds the size of square
        """
        def __init__(self, size):
            """ creates new instance of square.

            Args:
                size: size of square.
            """
        self.__size = size
