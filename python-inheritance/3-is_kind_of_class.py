#!/usr/bin/python3
"""
This module contains a function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class - returns if obj is a subclass of a_class"""


    return issubclass(type(obj), a_class)
