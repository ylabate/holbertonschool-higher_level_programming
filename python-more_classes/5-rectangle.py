#!/usr/bin/python3
"""Module defining a Rectangle class.

This module contains the definition of the Rectangle class,
which defines a rectangle by its width and height.
"""


class Rectangle:
    """Represents a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")

    @property
    def width(self):
        """int: Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: Retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter.

        Returns:
            int: The perimeter of the rectangle, or 0 if width or height is 0.
        """
        return (self.__width + self.__height
                ) * 2 if self.__width and self.__height else 0

    def __str__(self):
        """Returns the printable string representation of the rectangle.

        The rectangle is represented by the '#' character.

        Returns:
            str: The formatted string representing the rectangle.
        """
        res = ""
        if self.__width > 0 and self.__height:
            line = "#" * self.__width
            res += "\n".join(line for _ in range(self.__height))
        return res

    def __repr__(self):
        """Returns a string representation of the rectangle to recreate it."""
        return f"Rectangle({self.__width}, {self.__height})"


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

    del my_rectangle

    try:
        print(my_rectangle)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
