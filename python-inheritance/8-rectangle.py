#!/usr/bin/python3
"""
Module that defines a Rectangle class that inherits from BaseGeometry.
Provides a rectangle implementation with private width and height
attributes that are validated as positive integers.
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    A rectangle class that inherits from BaseGeometry.
    Represents a rectangle with private width and height attributes
    that are validated as positive integers.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle with width and height.

        :param width: The width of the rectangle (positive integer)
        :param height: The height of the rectangle (positive integer)
        :raise TypeError: If width or height is not an integer
        :raise ValueError: If width or height is not greater than 0
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
