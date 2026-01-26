#!/usr/bin/python3
"""Simple square module.

This module contains the definition of the Square class,
which keeps the a square in a private attribute.
"""


class Square:
    """Represents a square.

    This class stores the size of the square in a private attribute.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square.
                Defaults to (0, 0).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """tuple: Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints the string representation of the square to stdout.

        If the size is 0, prints an empty line. The position attribute is used to
        offset the square with spaces (horizontal) and newlines (vertical).
        """
        print(self.__str__(), end='')

    def __str__(self):
        """Returns the printable string representation of the square.

        This method constructs the square using the '#' character, applying the
        vertical offset (position[1]) and horizontal offset (position[0]).

        Returns:
            str: The formatted string representing the square. Returns a single
            newline character ('\\n') if the size is 0.
        """
        res = ""
        if self.__size > 0:
            res += "\n" * self.__position[1]
            line = " " * self.__position[0] + "#" * self.__size
            res += "\n".join(line for _ in range(self.__size)) + '\n'
        else:
            res += '\n'
        return res


if __name__ == "__main__":
    print("--")
    my_square = Square(5, (0, 0))
    print(my_square)

    print("--")

    my_square = Square(5, (4, 1))
    print(my_square)
