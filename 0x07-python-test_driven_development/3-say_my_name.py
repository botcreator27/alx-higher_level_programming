#!/usr/bin/python3

""" this module defines a function that prints out a person's full name """


def say_my_name(first_name, last_name=""):
    """
    Say_my_name function prints out full name in statement

    Args:
        first_name(str): person's first name
        last_name(str): person's last name

    Raises:
    TypeError: if either first_name or last_name is not str

    Returns:
        "my name is first_name + last_name"
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
