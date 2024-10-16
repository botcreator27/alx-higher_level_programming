#!/usr/bin/python3
""" module defines a function that adds attribute to class instance"""


def add_attribute(obj, attr_name, value):
    """
    adds a new attribute with value if possible
    Args:
        self: object
        attr_name(str): attribute name
        value: attribute value
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, value)
    raise TypeError(" can't add new attribute")
