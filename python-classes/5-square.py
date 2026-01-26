#!/usr/bin/python3
"""Simple square module.

This module contains the definition of the Square class,
which keeps the size of a square in a private attribute.
"""


class Square:
    """Represents a square.

    This class stores the size of the square in a private attribute.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.size = size

    def area(self):
        """Return the area of the square.

        Returns:
            int: The current area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """int: Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints the square using the '#' character.

        If size is 0, prints just a newline.
        """
        print("\n".join(("#" * self.__size) for _ in range(self.__size)))


if __name__ == "__main__":
    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")
