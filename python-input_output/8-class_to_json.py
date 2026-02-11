#!/usr/bin/python3
"""Module that returns the dictionary description with simple structure."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure.

    Args:
        obj: The object to serialize.

    Returns:
        dict: The dictionary description of the object.
    """
    return obj.__dict__
