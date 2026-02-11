#!/usr/bin/python3
"""Module that contains a function that reads a text file and prints it."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, "r") as file:
        print(file.read())
