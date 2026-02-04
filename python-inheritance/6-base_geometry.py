#!/usr/bin/python3
"""Module that defines a base geometry class for geometric shapes.

Provides the foundation class for creating geometric objects with
area calculation capability.
"""


class BaseGeometry:
    """
    A base class for geometry shapes that serves as the foundation
    for creating geometric objects.
    This class provides the basic structure and defines methods that
    subclasses must implement.
    """

    def area(self):
        """
        Calculate the area of the geometric shape.
        This method must be implemented by subclasses as it raises
        an exception in the base class.

        :raise Exception: This method is not implemented in the base
                         class and must be overridden
        """
        raise Exception("area() is not implemented")
