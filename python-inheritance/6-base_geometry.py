#!/usr/bin/python3
"""This module contains a class BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry, abstract class"""

    def area(self):
        """area - abstract method"""
        raise Exception("area() is not implemented")
