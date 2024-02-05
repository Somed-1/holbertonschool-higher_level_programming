#!/usr/bin/python3
"""This module contains class Rectangle"""


class Rectangle:
    """Class Rectangle"""
    def __init__(self, width=0, height=0) -> None:
        """
        __init__ - method to inicialize an instance of class
        Args:
            width: width of Rectangle
            height: height of Rectangle
        Return:
            nothing
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
