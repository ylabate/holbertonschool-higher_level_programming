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
    def __init__(self, size):
        """Initializes a new Square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size


if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)
