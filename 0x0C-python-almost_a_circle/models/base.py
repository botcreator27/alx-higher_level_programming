#!/usr/bin/python3
""" this module defines a class base """


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
