#!/usr/bin/python3
"""Module for converting CSV files to JSON format.

This module provides functionality to read data from CSV (Comma-Separated
Values) files and convert them into JSON format using Python's csv and json
modules. This is useful for transforming data between different formats and
enabling easier manipulation with JSON parsing libraries.

Functions:
    convert_csv_to_json: Converts a CSV file to JSON format.
"""

import csv
import json


def convert_csv_to_json(filename):
    """Convert a CSV file to JSON format and write to data.json.

    This function reads a CSV file where the first row contains column headers,
    converts each subsequent row into a dictionary with the headers as keys,
    and serializes the entire list of dictionaries to JSON format. The output
    is written to a file named 'data.json' in the current working directory.

    The function handles all exceptions gracefully and returns a boolean
    indicating success or failure, making it safe to use in production code
    without requiring explicit exception handling.

    Args:
        filename (str): The path or name of the CSV file to be converted.
                       The file should exist and be readable. The CSV file
                       must have headers in the first row.

    Returns:
        bool: True if the conversion was successful and data.json was
              created/updated. False if any error occurred during the
              process (file not found, permission denied, invalid CSV, etc.).
    """
    try:
        with open(filename, "r") as file:
            with open("data.json", "w") as result:
                json.dump(list(csv.DictReader(file)), result)
        return True
    except Exception:
        return False
