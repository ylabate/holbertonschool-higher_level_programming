#!/usr/bin/python3
"""Module that defines a rebel integer class.

This module provides MyInt, an integer class with inverted equality.
"""


class MyInt(int):
    """A rebel integer class that inverts equality and inequality operators.

    This class inherits from int but inverts the behavior of == and !=.
    """

    def __ne__(self, value: object) -> bool:
        """Invert the != operator to behave like ==.

        Args:
            value: The object to compare against.

        Returns:
            True if values are equal, False otherwise.
        """
        return not super().__ne__(value)

    def __eq__(self, value: object) -> bool:
        """Invert the == operator to behave like !=.

        Args:
            value: The object to compare against.

        Returns:
            True if values are not equal, False otherwise.
        """
        return not super().__eq__(value)
