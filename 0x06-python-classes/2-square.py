#!/usr/bin/python3
"""Module containing the Square class."""


class Square:

    """A class Square that defines a square."""

    def __init__(self, size=0):
        """Initialize a Square object with a given size."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
