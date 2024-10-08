#!/usr/bin/python3
""" this module defines a function that organizes text on new lines """


def text_indentation(text):
    """
    this function indents the text after identifying '.','?' and ':'
    characters

    Args:
        Text(str): the text to be indented

    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = []

    for char in text:
        if char in ".?:":
            result.append(char)
            result.append("\n\n")
        elif char == " " and (len(result) > 0 and result[-1] == "\n\n"):
            continue
        else:
            result.append(char)

    text = ''.join(result)
    print("{}".format(text), end="")
