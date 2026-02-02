#!/usr/bin/python3
"""
Module that defines a Rectangle class that inherits from BaseGeometry.
Provides a rectangle implementation with private width and height
attributes that are validated as positive integers.
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
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

    def print(self):
        print(self.__str__)
