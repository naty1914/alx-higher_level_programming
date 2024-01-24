#!/usr/bin/python3
"""Module containing the Square class."""


class Square:
    """A class Square that defines a square."""
    def __init__(self, size=0):
        """Initialize a Square object with a given size and position."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Compares two squares for equality based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compares two squares for inequality based on area."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Compares if one square is greater than another based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compares if one square is greater than or equal to another."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Compares if one square is less than another based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Compares if one square is less than or equal to another."""
        return self.area() <= other.area()
