#!/usr/bin/python3
""" this module reads a file and prints to stdout """


def read_file(filename=""):
    """  reads a text file (UTF8) and prints it to stdout """
    with open(filename, "r", encoding="utf-8") as a_file:
        print(a_file.read())
