#!/usr/bin/python3
"""This module contains class Base"""
import json


class Base:
    """class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        __init__ method of class Base
        """
        if id is None:
            self.increase_nb()
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries, skipkeys=True)

    @classmethod
    def increase_nb(cls):
        cls.__nb_objects += 1
