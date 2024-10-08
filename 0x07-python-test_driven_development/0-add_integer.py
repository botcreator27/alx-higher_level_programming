#!/usr/bin/python3

"""
    this module defines a function that adds two intergers
    Examples:
    >>> add_integer(1, 1)
    2
    >>> add_integer(-1, 1)
    0
"""


def add_integer(a, b=98):
    """
    function add_integer adds two integers, a and b

    Args:
        a(int): first number
        b(int): second number

    Raises:
        TypeError: if a, b are neither int nor float

    Returns:
        sum of int a and int b

    Examples:
    >>> add_integer("1", 2)
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer
    >>> add_integer(1, "2")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    >>> add_integer(5.0)
    103
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return ((a) + (b))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
