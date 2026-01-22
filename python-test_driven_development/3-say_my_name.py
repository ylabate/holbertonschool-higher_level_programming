#!/usr/bin/python3
"""
That a module that contains say_my_name is a function that print
"My name is" with the first and last name
"""


def say_my_name(first_name, last_name=""):
    """Print a formatted name string.

    This function prints "My name is <first_name> <last_name>"
    to the standard output.

    Args:
        first_name (str): The first name to print. Cannot be empty.
        last_name (str, optional): The last name to print. Defaults to "".

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.

    Examples:
        >>> say_my_name("John", "Smith")
        My name is John Smith$
        >>> say_my_name("Bob")
        My name is Bob $
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif last_name:
        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name if last_name else ''}")
