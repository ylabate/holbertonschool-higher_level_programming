#!/usr/bin/env python3
"""Module that checks if an object is an instance of a specified class."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a specified class.

    This function checks if obj is an instance of, or inherited from,
    the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or inherited from it,
        False otherwise.
    """
    return isinstance(obj, a_class)
