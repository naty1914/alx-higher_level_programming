#!/usr/bin/python3
"""  module  that contains  a function that checks if an object
is an instance of a class"""


def is_same_class(obj, a_class):
    """  Checks if an object is an exact instance of the class"""
    return type(obj) is a_class
