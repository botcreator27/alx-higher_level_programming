#!/usr/bin/python3
""" this module reverts a json format to original"""
import json


def from_json_string(my_str):
    """ function reverts from json format to obj
    Args:
        my_str: json format
    """
    return json.loads(my_str)
