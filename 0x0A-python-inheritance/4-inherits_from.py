#!/usr/bin/python3
"""  module  that contains  a function that checks if an object
is an instance of a class"""


def inherits_from(obj, a_class):
    """ Check if obj is an instance of a class that inherited
     from the specified class"""

    return isinstance(obj, a_class) and type(obj) is not a_class
