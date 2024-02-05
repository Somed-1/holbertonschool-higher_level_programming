#!/usr/bin/python3
"""This module contains class Rectangle"""


class Rectangle:
    number_of_instances = 0
    """Class Rectangle"""
    def __init__(self, width=0, height=0):
        """
        __init__ - method to inicialize an instance of class
        Args:
            width: width of Rectangle
            height: height of Rectangle
        Return:
            nothing
        """
        self.number_of_instances += 1
        self.width = width
        self.height = height

    def area(self):
        """
        area - return area of Rectangle
        Return:
            area of Rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        perimeter - returns perimeter of Rectangle
        Return:
            perimeter of Rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2 + self.height * 2)

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

    def __str__(self):
        if self.__width == 0 or self.height == 0:
            return ""
        return "\n".join("#" * self.width for i in range(self.height))

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        self.number_of_instances -= 1
        print("Bye rectangle...")
