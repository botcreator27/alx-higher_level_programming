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

    Returns:
        sum of int a and int b

    Both a and b must be an int or float, else raise TypeError
    If a and b are float they must be casted into integers
    Function should be able to add neg integers

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
    doctest.testmod()

