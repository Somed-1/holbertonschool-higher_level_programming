#!/usr/bin/python3
"""This module contains class Student"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, keys=None):
        if keys is not None:
            if all(isinstance(i, str) for i in keys):
                n = {k: getattr(self, k) for k in keys if hasattr(self, k)}
                return n
        return self.__dict__

    def reload_from_json(self, json):
        for k, v in json.items():
            setattr(self, k, v)
