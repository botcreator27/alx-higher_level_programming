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

    def area(self):
        """ Returns the sq are of the square

            Returns: the sq area
        """
        return self.__size ** 2

    @property
    def size(self):
        """Returns the size of the squre which is private"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        property setter for size

        Args:
            value(int): size to be set
        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        prints size of the square with #
 
        """
        for x in range(self.__size):
            print("#" * self.__size)
