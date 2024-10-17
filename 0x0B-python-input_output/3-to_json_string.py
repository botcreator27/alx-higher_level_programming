#!/usr/bin/python3
""" module converts to json format """
import json


def to_json_string(my_obj):
    """ funicction returns the json format of my_obj
    Args:
        my_obj: python object
    """
    return json.dumps(my_obj)
