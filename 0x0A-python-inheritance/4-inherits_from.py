#!/usr/bin/python3
""" this module checks for instance of subclasses"""


def inherits_from(obj, a_class):
    """ checks if obj is instance of subclass of specified class
    Args:
        obj: the object
        a_class: the specified class
    Returns:
        true - if is instance of subclass but not a_class, fail- if not
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
