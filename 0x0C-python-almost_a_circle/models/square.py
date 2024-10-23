#!/usr/bin/python3
from models.rectangle import Rectangle
""" this module defines class square- a rectangle subclass"""


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
