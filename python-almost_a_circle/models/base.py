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
        """to_json_string method of class Base"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return []

    @classmethod
    def increase_nb(cls):
        cls.__nb_objects += 1
