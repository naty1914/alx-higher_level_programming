#!/usr/bin/python3
"""A module for loading data from a JSON file."""

import json


def load_from_json_file(filename):
    """
    Load data from a JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
