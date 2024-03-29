#!/usr/bin/python3
"""This module contains add_attribute function"""


def add_attribute(instance, name, value):
    """add_attribute function"""

    if hasattr(instance, "__dict__"):
        setattr(instance, name, value)
    else:
        raise TypeError("can't add new attribute")
