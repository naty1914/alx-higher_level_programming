#!/usr/bin/python3
"""Module for appending text to a file."""


def append_write(filename="", text=""):
    """
    Append text to a file.
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
