#!/usr/bin/python3
"""
Module that demonstrates duck typing with abstract base classes.

This module shows how to use abstract base classes to define a Shape
interface and implement concrete shapes like Circle and Rectangle.
It includes a shape_info function that demonstrates duck typing by
accepting any object that implements the Shape interface.
"""
from abc import ABC, abstractmethod
pi = 3.141592653589793


class Shape(ABC):
    """
    An abstract base class defining the interface for geometric shapes.

    This class establishes the contract that all shape subclasses must
    implement to calculate their area and perimeter.
    """

    @abstractmethod
    def area(self) -> float:
        """
        Calculate and return the area of the shape as a formatted string.

        Returns:
            str: A string representation of the shape's area.

        Raises:
            NotImplementedError: This method must be implemented by
                                 concrete subclasses.
        """
        ...

    @abstractmethod
    def perimeter(self) -> float:
        """
        Calculate and return the perimeter of the shape as a formatted string.

        Returns:
            str: A string representation of the shape's perimeter.

        Raises:
            NotImplementedError: This method must be implemented by
                                 concrete subclasses.
        """
        ...


class Circle(Shape):
    """A concrete implementation of Shape representing a circle.

    This class provides the abstract methods of Shape to calculate
    the area and perimeter of a circle based on its radius.
    """

    def __init__(self, radius):
        """
        Initialize a Circle with a given radius.

        Args:
            radius: The radius of the circle (must be an integer).

        Raises:
            TypeError: If radius is not an integer.
        """
        if type(radius) is int:
            self.__radius = radius
        else:
            raise TypeError("radius should be a integer")

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            str: A formatted string containing the area calculation.
        """
        return (self.__radius ** 2) * pi

    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.

        Returns:
            str: A formatted string containing the perimeter calculation.
        """
        return 2 * pi * self.__radius


class Rectangle(Shape):
    """A concrete implementation of Shape representing a rectangle.

    This class provides the abstract methods of Shape to calculate
    the area and perimeter of a rectangle based on its dimensions.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle with given width and height.

        Args:
            width: The width of the rectangle (must be an integer).
            height: The height of the rectangle (must be an integer).

        Raises:
            TypeError: If width or height is not an integer.
        """
        if type(width) is int:
            self.__width = width
        else:
            raise TypeError("width should be a integer")
        if type(height) is int:
            self.__height = height
        else:
            raise TypeError("height should be a integer")

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            str: A formatted string containing the area calculation.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            str: A formatted string containing the perimeter calculation.
        """
        return self.__width * 2 + self.__height * 2


def shape_info(shape):
    """Print the area and perimeter information of a shape.

    This function demonstrates duck typing by accepting any object
    that has area() and perimeter() methods, regardless of whether
    it explicitly inherits the Shape class.

    Args:
        shape: An object that provides area() and perimeter() methods.

    Raises:
        TypeError: If the shape object does not have the required methods.
    """
    try:
        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}")
    except TypeError:
        raise TypeError("shape should be a child of Shape")
