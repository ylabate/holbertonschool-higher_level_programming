#!/usr/bin/env python3
"""Module that defines a base geometry class for geometric shapes.

Provides the foundation class for creating geometric objects with
area calculation and integer validation capabilities.
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

    def integer_validator(self, name, value):
        """
        Validate that a value is a positive integer.

        :param name: The name of the parameter being validated
        :param value: The value to validate
        :raise TypeError: If value is not an integer
        :raise ValueError: If value is not greater than 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
