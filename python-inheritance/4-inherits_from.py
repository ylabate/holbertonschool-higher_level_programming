#!/usr/bin/python3
"""Module that checks if an object is an instance of a subclass.

Provides a function to check if an object is an instance of a class
that inherited from the specified class.
"""


def inherits_from(obj, a_class):
    """Check if object is an instance of a class that inherited.

    Returns True only if the object's class is a subclass of a_class,
    not if it is directly an instance of a_class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is instance of a class that inherited from a_class,
        False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
