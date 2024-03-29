#!/usr/bin/python3
"""This module contains the function taht prints square"""


def print_square(size):
    """
    print_square - prints square usign #
    Args:
        size: the size of square (int)
    Return:
        Nothing
    """
    if not isinstance(size, (int)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        print("{}".format("#" * size))
