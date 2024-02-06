#!/usr/bin/python3
"""Module MyClass"""


class MyClass:
    """ Represents a simple class"""

    def __init__(self, name):
        self.name = name
        self.number = 0

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)


def class_to_json(obj):
    """Converts an instance of a Class to a dictionary
       description for JSON serialization.
    """
    json_dictionary = {}
    for attr_name in dir(obj):
        if not attr_name.startswith('__'):
            attr_value = getattr(obj, attr_name)
            if isinstance(attr_value, (list, dict, str, int, bool)):
                json_dictionary[attr_name] = attr_value
    return json_dictionary
