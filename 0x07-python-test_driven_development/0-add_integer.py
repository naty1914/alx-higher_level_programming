#!/usr/bin/python3
"""This is the module docstring.

It provides a function called add_integer to perform addition.

"""

def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    return a + b
