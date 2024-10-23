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
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ returns the json format of a list of class instances
            to a file
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write(cls.to_json_string([]))
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ converts arg(json string) to obj"""
        if json_string is not None:
            return json.loads(json_string)
        return "[]"
