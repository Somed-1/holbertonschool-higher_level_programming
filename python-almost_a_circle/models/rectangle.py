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

    def area(self):
        """area method of class Rectangle"""
        return self.width * self.height

    def display(self):
        """display method of class Rectangle"""
        [print("#"*self.width) for i in range(self.height)]

    def check_size(self, name, value):
        """check_size method to check size"""
        if not isinstance(value, (int, )):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def check_cords(self, name, value):
        """check_cords method to check cords"""
        if not isinstance(value, (int, )):
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    @property
    def width(self):
        """width attribute of class Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.check_size("width", value)
        self.__width = value

    @property
    def height(self):
        """height attribute of class Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.check_size("height", value)
        self.__height = value

    @property
    def x(self):
        """x attribute of class Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        self.check_cords("x", value)
        self.__x = value

    @property
    def y(self):
        """y attribute of class Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self.check_cords("y", value)
        self.__y = value

    def __str__(self) -> str:
        """__str__ method of class Rectangle"""
        template = "[Rectangle] ({}) {}/{} - {}/{}"
        return template.format(
            self.id, self.x,
            self.y, self.width,
            self.height)
