#!/usr/bin/python3
"""Module containing the rectangle class."""


class Rectangle:
    """   class  that defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle."""

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the  rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Return a string representation of the rectangle using char #."""
        if self.__width == 0 or self.__height == 0:
            return ''
        string_result = ''
        for x in range(self.__height):
            string_result += '#' * self.__width + '\n'
        return string_result[:-1]

    def __repr__(self):
        """Returns a string representation  recreate the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"
