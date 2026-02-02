"""
Module that provides a VerboseList class for tracking list modifications.

This module defines a custom list subclass that prints informative
messages whenever the list is modified through append, extend, remove,
or pop operations. It demonstrates method overriding and the use of
super() to retain original functionality while adding custom behavior.
"""
from typing import SupportsIndex


class VerboseList(list):
    """
    A custom list class that prints notifications for all modifications.

    This class extends the built-in list class and overrides methods that
    modify the list to print informative messages about each operation.
    """

    def append(self, item):
        """
        Append an item to the list and print a notification.

        Args:
            item: The item to append to the list.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, item):
        """
        Extend the list with multiple items and print a notification.

        Args:
            item: An iterable of items to add to the list.
        """
        super().extend(item)
        print(f"Extended the list with [{len(item)}] items.")

    def remove(self, item):
        """
        Remove an item from the list and print a notification.

        Args:
            item: The item to remove from the list.

        Raises:
            ValueError: If the item is not in the list.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index: SupportsIndex = -1):
        """
        Remove and return an item at the given index and print a notification.

        Args:
            index: The index of the item to pop (default: -1 for last item).

        Returns:
            The item that was removed from the list.
        """
        value = self[index]
        print(f"Popped [{value}] from the list.")
        return super().pop(index)
