#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file.

        Args:
            filename(txt): the name of the file
    """
    with open(filename) as fileobj:
        return json.load(fileobj)
