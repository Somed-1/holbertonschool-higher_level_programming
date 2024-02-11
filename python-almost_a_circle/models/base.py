#!/usr/bin/python3
"""This module contains class Base"""


class Base:
    """class Base"""

    __nb_objects = 0
    def __init__(self, id=None) -> None:
        if id is None:
            self.increase_nb()
            self.id = self.__nb_objects
        else:
            self.id = id

    @classmethod
    def increase_nb(cls):
        cls.__nb_objects += 1
