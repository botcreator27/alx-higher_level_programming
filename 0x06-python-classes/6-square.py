#!/usr/bin/python3
""" Define the Class Square"""


class Square:
    """
    Defines properties of square (based on 0-square.py).

    Attributes:
        __size(int): size of square.
        __position(tuple): tuple of 2 positve ints
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialises the class square (1 side).

        Args:
            size: size of square.
            position: tuple os 2 positive ints.
        """
        self.__size = size
        self.__position = position

    def area(self):
        """ Returns the sq are of the square

            Returns: the sq area
        """
        return self.__size ** 2

    @property
    def size(self):
        """Returns the size of the squre which is private"""
        return self.__size
    @property
    def position(self):
        """Returns position attribute"""
        return self.__position

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

    @position.setter
    def position(self, value):
        """
        property setter for position

        Args:
            value(tuple): position value
        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if not isinstance(position, tuple) or if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value

    def my_print(self):
        """ prints size of the square with # """
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for x in range(self.__size):
                for k in range(self.position[0]):
                    print(" ", end="")
                print("#" * (self.__size))
