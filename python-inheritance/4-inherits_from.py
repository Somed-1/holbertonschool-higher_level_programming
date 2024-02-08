#!/usr/bin/python3
"""This module contains a function inherits_from"""


def inherits_from(obj, a_class):
    """inhertis_from - returns if is an instance of a class"""

    return False if type(obj) is a_class else isinstance(obj, a_class)
