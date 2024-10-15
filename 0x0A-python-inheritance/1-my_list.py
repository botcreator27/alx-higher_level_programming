#!/usr/bin/python3"
"""this module describes a class Mylist """


class MyList(list):
    """ this class inherits from list """
    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        print(sorted(self))
