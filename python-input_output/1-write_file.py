#!/usr/bin/python3
"""Module that contains a function that writes a string to a text file."""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of chars.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w") as file:
        return file.write(text)
