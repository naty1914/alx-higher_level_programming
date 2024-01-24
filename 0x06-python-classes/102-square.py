#!/usr/bin/python3
"""Module containing the Square class."""


class Square:
    """A class Square that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square object with a given size and position."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square."""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(x, int) for x in value) or \
                not all(x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with '#' character."""
        if self.__size == 0:
            print()
            return
        else:
            for x in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(" " * self.__position[0] + '#' * self.__size)
