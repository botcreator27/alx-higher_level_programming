#!/usr/bin/python3
""" this module defines a function that prints out a square with # """


def print_square(size):
    """
    print_square - prints the size of the square with #

    Args:
        size(int): the length of the square

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
        TypeError: if size is float and < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0 :
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for x in range(size):
        print("#" * size)
