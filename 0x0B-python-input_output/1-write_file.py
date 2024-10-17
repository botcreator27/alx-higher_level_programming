#!/usr/bin/python3
""" this module describes a write function """


def write_file(filename="", text=""):
    """ writes to a file(overwrites if already existing)
    Args:
        filename: filename
        text(str): text to be written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
