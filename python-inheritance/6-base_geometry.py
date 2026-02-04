#!/usr/bin/python3
"""Module that defines a base geometry class for geometric shapes.

Provides the foundation class for creating geometric objects with
area calculation capability.
"""


class BaseGeometry:
    """A base class for geometry shapes.

    This class provides the basic structure and defines methods that
    subclasses must implement.
    """

    def area(self):
        """Calculate the area of the geometric shape.

        This method must be implemented by subclasses.

        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")
