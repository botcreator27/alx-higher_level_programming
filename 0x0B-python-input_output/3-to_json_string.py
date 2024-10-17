#!/usr/bin/python3
import json
""" module converts to json format """


def to_json_string(my_obj):
    """ funicction returns the json format of my_obj
    Args:
        my_obj: python object 
    """
    return json.dumps(my_obj)
