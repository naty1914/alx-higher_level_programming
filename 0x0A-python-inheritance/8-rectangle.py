#!/usr/bin/python3
"""  module  that contains  class BaseGeometry   and it's method"""


class BaseGeometry:
    """ class BaseGeometry"""
    def area(self):
        """Public instance method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Represents a rectangle with private width and height attributes.
    """

    def __init__(self, width, height):
        super().__init__()
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
