#!/usr/bin/python3
""" Define the Class Square"""


class Square:
    """
    Defines properties of square (based on 0-square.py).

    Attributes:
        __size(int): size of square.
    """
    def __init__(self, size=0):
        """
        Initialises the class square (1 side).

        Args:
            size: size of square.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
