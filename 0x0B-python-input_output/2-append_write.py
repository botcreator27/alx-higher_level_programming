#!/usr/bin/python3
""" this module writes a function which appends to a file"""


def append_write(filename="", text=""):
    """ function appends to a file
    Args:
        filename: filename
        text: text to be appended
    """
    with open(filename, "a", encoding="utf-8"):
        return f.write(text)
