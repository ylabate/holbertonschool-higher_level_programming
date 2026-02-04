#!/usr/bin/python3
"""
Module that provides a function to check
if an object is an instance of a subclass.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class
    that inherited from the specified class.
    Returns True only if the object's class is a subclass of a_class,
    not if it is directly an instance of a_class.

    :param obj: The object to check
    :param a_class: The class to check against
    :return: True if obj is an instance of a class that inherited from a_class,
    False otherwise
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
