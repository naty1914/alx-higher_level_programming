#!/usr/bin/python3
"""Script to add command-line arguments to a JSON file."""

import sys
from os import path


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

if path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

items.extend(sys.argv[1:])
save_to_json_file(items, filename)
