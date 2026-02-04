#!/usr/bin/python3
"""Module that defines a Rectangle class.

This module provides a Rectangle class that inherits from BaseGeometry
with private width and height attributes validated as positive integers.
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class that inherits from BaseGeometry.

    This class represents a rectangle with private width and height
    attributes that are validated as positive integers.
    """

    def __init__(self, width, height):
        """Initialize a Rectangle with width and height.

        Args:
            width: The width of the rectangle (positive integer).
            height: The height of the rectangle (positive integer).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not greater than 0.
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
