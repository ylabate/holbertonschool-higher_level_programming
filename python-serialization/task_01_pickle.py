#!/usr/bin/python3
"""Module for serializing and deserializing custom objects using pickle.

This module provides a CustomObject class that can be serialized to and
deserialized from files using the pickle module. It demonstrates how to
work with pickle for object persistence.
"""

import pickle


class CustomObject:
    """A custom class that can be serialized and deserialized using pickle.

    This class represents a person with basic attributes and provides
    methods to serialize the instance to a file and deserialize it back.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): Whether the person is a student.
    """

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject with name, age, and student status.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes in a formatted way.

        Prints the object's name, age, and student status to stdout
        in a human-readable format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance and save it to a file.

        Uses the pickle module to serialize the current instance and
        save it to the specified file. If an error occurs (such as
        file permission issues), the method returns None silently.

        Args:
            filename (str): The filename to save the serialized object to.

        Returns:
            None: Always returns None
            (implicitly on success, explicitly on error).
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file.

        Uses the pickle module to load and deserialize an object from
        the specified file. If the file does not exist or is malformed,
        the method returns None instead of raising an exception.

        Args:
            filename (str): The filename to load the serialized object from.

        Returns:
            CustomObject: The deserialized object instance, or None if
                         the file could not be read or is malformed.
        """
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception:
            return None
