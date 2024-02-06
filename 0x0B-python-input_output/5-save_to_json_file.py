#!/usr/bin/python3
""" module that Save Object to a file"""
import json
import os


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation."""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
