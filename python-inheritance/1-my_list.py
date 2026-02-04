#!/usr/bin/python3
"""
Module that defines a MyList class that inherits from the built-in list class.
Provides functionality to work with lists and print them in sorted order.
"""


class MyList(list):
    """
    A class that inherits from the built-in list class and extends
    its functionality.
    Provides a method to print the list elements in sorted order
    without modifying the original list.
    """

    def print_sorted(self):
        """
        Print the list elements in sorted order in ascending sequence.
        This method does not modify the original list,
        only displays the sorted version.
        """
        print(sorted(self))
