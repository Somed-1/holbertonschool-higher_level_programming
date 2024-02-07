#!/usr/bin/python3
"""This module contains lookup function"""


def lookup(obj):
    """
    lookup - returns object's all attributes
    Args:
        obj: object
    Return:
        list of attributes
    """
    return dir(obj)
