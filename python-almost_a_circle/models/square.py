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
        template = "[Square] ({}) {}/{} - {}/{}"
        return template.format(
            self.id, self.x,
            self.y, self.width,
            self.height)
