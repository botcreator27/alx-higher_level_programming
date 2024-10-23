#!/usr/bin/python3
""" this module defines a class base """
import json


class Base:
    """ base class for other classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ initialises id attribute
        Args:
            id: id attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json format of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return []
        return json.dumps(list_dictionaries)
