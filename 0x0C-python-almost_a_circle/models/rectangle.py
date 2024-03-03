#!/usr/bin/python3

""" A module  of a class inheritance"""
from models.base import Base


class Rectangle(Base):
    """ A class rectangle that inherits from class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ It initializes a rectangle instance """
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """A getter property for width """
        return self.__width

    @width.setter
    def width(self, width):
        """A setter property for width """
        self.__width = width

    @property
    def height(self):
        """A getter property for height """
        return self.__height

    @height.setter
    def height(self, height):
        """A setter property for height """
        self.__height = height

    @property
    def x(self):
        """A getter property for x """
        return self.__x

    @x.setter
    def x(self, x):
        """A setter property for x """
        self.__x = x

    @property
    def y(self):
        """A getter property for y """
        return self.__y

    @y.setter
    def y(self, y):
        """A setter property for y """
        self.__y = y
