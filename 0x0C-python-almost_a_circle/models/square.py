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
