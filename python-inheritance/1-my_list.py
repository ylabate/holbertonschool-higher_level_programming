#!/usr/bin/python3
"""Module that defines a MyList class.

This module provides a MyList class that inherits from the built-in
list class and provides functionality to print sorted lists.
"""


class MyList(list):
    """A class that inherits from the built-in list class.

    This class extends list functionality by providing a method to
    print list elements in sorted order without modifying the original.
    """

    def print_sorted(self):
        """Print the list elements in sorted ascending order.

        This method does not modify the original list.
        """
        print(sorted(self))
