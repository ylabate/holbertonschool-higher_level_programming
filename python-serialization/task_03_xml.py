#!/usr/bin/python3
"""Module for serializing and deserializing Python dictionaries using XML.

This module provides functionality to convert Python dictionaries to XML format
and back, using Python's xml.etree.ElementTree module. This enables easy storage
and retrieval of structured data in XML files.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to XML format and save to a file.

    Converts a Python dictionary into an XML representation where each
    key-value pair becomes an XML element. The XML structure uses a root
    element named 'data' containing all dictionary items as child elements.

    Args:
        dictionary (dict): A dictionary to be serialized. Keys should be
                          valid XML element names (strings without special
                          characters). Values are converted to strings.
        filename (str): The path to the output XML file. Can be absolute or
                       relative path. The file will be created if it doesn't
                       exist, or overwritten if it already exists.

    Returns:
        None: The function writes directly to the file and does not return
              a value.
    """
    root = ET.Element("data")
    for key, item in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(item)
    with open(filename, "wb") as file:
        ET.ElementTree(root).write(file)


def deserialize_from_xml(filename):
    """Deserialize an XML file back into a Python dictionary.

    Reads an XML file and converts it back to a Python dictionary format.
    Expects the XML to have a root element with child elements where each
    child element's tag becomes a dictionary key and its text content
    becomes the corresponding dictionary value.

    Args:
        filename (str): The path to the XML file to deserialize. Can be
                       absolute or relative path. The file must exist and
                       contain valid XML data with a root element containing
                       child elements.

    Returns:
        dict: A dictionary reconstructed from the XML file where keys are
              element tags and values are element text content. Returns an
              empty dictionary if the XML root has no child elements.
    """
    with open(filename, "r") as file:
        return {child.tag: child.text for child in ET.parse(file).getroot()}

