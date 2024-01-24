#!/usr/bin/python3
"""Module containing the Square class."""
import math


class MagicClass:

    """A class with radius-based area and circumference calculation."""
    def __init__(self, radius):
        """Initializes the instance with a radius."""
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area of the circle."""
        return math.pi * self.__radius**2

    def circumference(self):
        """Returns the circumference of the circle."""
        return 2 * math.pi * self.__radius
