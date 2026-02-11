#!/usr/bin/python3
"""Module that contains a function that creates an Object from a JSON file."""

import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”.

    Args:
        filename (str): The name of the file to read.

    Returns:
        object: The object represented by the content of the file.
    """
    with open(filename, "r") as file:
        return json.load(file)
