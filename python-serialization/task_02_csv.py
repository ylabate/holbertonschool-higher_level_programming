#!/usr/bin/python3
"""Module for converting CSV files to JSON format.

This module provides functionality to read CSV files and convert them
to JSON format, making it easy to work with CSV data as JSON objects.
"""

import csv
import json


def convert_csv_to_json(filename):
    """Convert a CSV file to JSON format.

    Reads a CSV file and converts it to JSON format, saving the result
    to a file named 'data.json'. Each row in the CSV file is converted
    to a dictionary in the JSON output.

    Args:
        filename (str): The path to the CSV file to be converted.

    Returns:
        None: The function writes the JSON data directly to 'data.json'
              and does not return a value.

    Raises:
        FileNotFoundError: If the specified CSV file does not exist.
        IOError: If there is an error reading the CSV file or writing
                 the JSON file.

    Example:
        >>> convert_csv_to_json('input.csv')
        # Creates 'data.json' with the CSV data in JSON format
    """
    with open(filename, "r") as file:
        with open("data.json", "w") as result:
            json.dump(list(csv.DictReader(file)), result)
