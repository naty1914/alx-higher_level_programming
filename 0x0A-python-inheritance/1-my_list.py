#!/usr/bin/python3
"""A module about a inheritance"""


class MyList(list):
    """ A class the inherits a list."""
    def print_sorted(self):
        """ A function prints the list in sort."""
        print(sorted(self))
