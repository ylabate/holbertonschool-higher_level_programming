#!/usr/bin/python3
"""Module that contains a function that appends a string."""


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF8) and returns the number of chars.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a") as file:
        return file.write(text)
