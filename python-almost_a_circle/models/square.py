#!/usr/bin/python3
"""This module contains class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """__init__ method of class Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """__str__ method of class Square"""
        template = "[Square] ({}) {}/{} - {}"
        return template.format(
            self.id, self.x,
            self.y, self.width
        )

    def update(self, *args, **kwargs):
        """update method of class Square"""
        if args:
            attributes = ["id", "size", "x", "y"]
            attributes = zip(attributes, args)
            for attr in attributes:
                setattr(self, attr[0], attr[1])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """to_dictionary method of class Square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
