#!/usr/bin/python3
"""module create an obj rom json file"""
import json


def load_from_json_file(filename):
    """ function converts json file to obj
    Args:
        filename: the json file
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f)
