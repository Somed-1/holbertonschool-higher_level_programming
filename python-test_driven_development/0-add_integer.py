#!/usr/bin/python3
"""This module contains the function that adds two numbers"""


def add_integer(a, b=98):
    """
    add_integer - adds two integers only
    Args:
        a: first number (int, flaot)
        b: second number (int, float)
    Return:
        The sum of two integers (integer)
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
