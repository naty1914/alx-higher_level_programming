#!/usr/bin/python3
"""Module for writing to a file."""


def write_file(filename="", text=""):
    """
    Write text to a file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
