#!/usr/bin/python3
"""This module contains class Student"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, *args):
        if args:
            if args[0]:
                return {key: self.__dict__.get(key) for key in args[0]}
            else:
                return type(self)
        return self.__dict__
