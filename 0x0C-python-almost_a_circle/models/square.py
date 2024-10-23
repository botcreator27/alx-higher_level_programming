#!/usr/bin/python3
""" this module defines class square- a rectangle subclass"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialises attributes
            Args:
                size: size of square
                x: x
                y: y
                id: id number of instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """displays a Square details"""
        return "[Square] (<{}>) <{}>/<{}> - size".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value
 
    def __update(self, id=None, size=None, x=None, y=None):
        """private method to set attributes"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """method to assign attributes"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)
