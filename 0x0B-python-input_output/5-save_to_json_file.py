#!/usr/bin/python3
""" module write abj as a json str to file """
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file
    Args:
        my_obj: object
        filename:file we're writing to
    """
    with open(filename, "w", encoding="utf-8"):
        json.dump(my_obj, filename)
