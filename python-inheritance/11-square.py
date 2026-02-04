#!/usr/bin/python3
"""Module that defines a Square class.

This module provides a Square class that inherits from Rectangle
and represents a square with equal sides.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class that inherits from Rectangle.

    This class represents a square with all sides of equal length.
    """

    def __init__(self, size):
        """Initialize a Square with size.

        Args:
            size: The size of the square sides (positive integer).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not greater than 0.
        """
        super().__init__(size, size)

    def __str__(self):
        """Return the string representation of the square.

        Returns:
            A string in the format [Square] <size>/<size>.
        """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
