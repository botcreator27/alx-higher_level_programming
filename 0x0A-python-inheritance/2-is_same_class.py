#!/usr/bin/python3
""" this module defines a function that check instances of a class """


def is_same_class(obj, a_class):
    """function checks is obj is an instance of class

    Args:
        obj: the object
        a_class: the class to be ckecked against

    Returns:
        True for success, False for not instance
        """
    if type(obj) is a_class:
        return True
    return False
