#!/usr/bin/python3
"""This module contains class Rectangle."""
from models.base import Base


class Rectangle(Base):
    """class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ method of class Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def _check_size(self, name, value):
        """_check_size method to check size"""
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be >= 0")

    def _check_cords(self, name, value):
        """_check_cords method to check cords"""
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be > 0")

    @property
    def width(self):
        """width attribute of class Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self._check_size("width", value)
        self.__width = value

    @property
    def height(self):
        """height attribute of class Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self._check_size("height", value)
        self.__height = value

    @property
    def x(self):
        """x attribute of class Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        self._check_cords("x", value)
        self.__x = value

    @property
    def y(self):
        """y attribute of class Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self._check_cords("y", value)
        self.__y = value
