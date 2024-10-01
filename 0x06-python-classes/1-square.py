#!/usr/bin/python3
""" Define the Class Square"""


class Square:
    """
    Defines properties of square (based on 0-square.py).

    Attributes:
        __size(int): size of square.
    """
    def __init__(self, size):
        """
        Initialises the class square (1 side).

        Args:
            size: size of square.
        """
        self.__size = size
