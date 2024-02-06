#!/usr/bin/python3
""" module that returns JSON string to Object"""
import json
import os


def from_json_string(my_str):
    """A function hat returns an object
       represented by a JSON string.
    """
    return json.loads(my_str)
