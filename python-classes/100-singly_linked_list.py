#!/usr/bin/python3
"""Singly linked list module.

This module contains the definitions for Node and SinglyLinkedList classes.
"""


class Node:
    """Represents a node of a singly linked list.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node): The next node in the list.
    """

    def __init__(self, data, next_node=None):
        """Initializes a new Node.

        Args:
            data (int): The data of the node.
            next_node (Node, optional): The next node in the list.
                Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data attribute of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data attribute of the node.

        Args:
            value (int): The new data for the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next_node attribute."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next_node attribute.

        Args:
            value (Node): The new next_node. Can be None.

        Raises:
            TypeError: If value is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list.

    Attributes:
        __head (Node): The head of the linked list.
    """

    def __init__(self):
        """Initializes a new, empty SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position (increasing order).

        Args:
            value (int): The value for the new Node.
        """
        if not self.__head:
            self.__head = Node(value)
        else:
            head = self.__head
            if head.data >= value:
                self.__head = Node(value, head)
                return
            prev_head = head
            while head:
                if value <= head.data:
                    prev_head.next_node = Node(value, head)
                    return
                prev_head = head
                head = head.next_node
            prev_head.next_node = Node(value)

    def __str__(self):
        """Generates the string representation of the linked list.

        The list is represented with one node's data per line.

        Returns:
            str: The string representation of the list.
        """
        res = ""
        local_head = self.__head
        while local_head:
            res += str(local_head.data)
            if local_head.next_node:
                res += '\n'
            local_head = local_head.next_node
        return res


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)

    print(sll)
