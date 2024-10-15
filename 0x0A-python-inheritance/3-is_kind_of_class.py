#!/usr/bin/python3
""" this module defines a function that checks for instance of object """


def is_kind_of_class(obj, a_class):
    """ checks if obj is instance of class or subclass of class
    Args:
        obj: the object
        a_class: the class in question
    Returns:
        True- sucess, False -not instance
    """
    return isinstance(obj, a_class)
