#!/usr/bin/python3
"""This module contains add_attribute function"""


def add_attribute(instance, name, value):
    """add_attribute function"""

    try:
        setattr(instance, name, value)
    except AttributeError:
        raise TypeError("can't add new attribute")
