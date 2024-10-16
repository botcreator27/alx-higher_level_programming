#!/usr/bin/python3
""" this module creates class MyInt"""


class MyInt(int):
    """ class MyInt is a subclass of int """
    def __eq__(self, other):
        """ == oprator but reversed"""
        if isinstance(other, int):
            return int.__ne__(self, other)

    def __ne__(self, other):
        """ != operator reversed """
        if isinstance(other, int):
            return int.__eq__(self, other)
