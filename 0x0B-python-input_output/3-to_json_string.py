#!/usr/bin/python3
""" module that returns the  JSON retpresention to string"""
import json
import os


def to_json_string(my_obj):
    """A function function that returns the
       JSON representation of an object (string).
    """
    return json.dumps(my_obj)
