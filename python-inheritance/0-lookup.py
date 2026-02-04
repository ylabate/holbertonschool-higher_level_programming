#!/usr/bin/python3
"""
Module for looking up attributes and methods of objects.
Provides a function to return a list of all attributes and methods of any object.
"""


def lookup(obj):
    """
    Return a list of available attributes and methods of an object.

    :param obj: Any object to inspect
    :return: List of strings containing the names of all attributes and methods
    """
    return dir(obj)
