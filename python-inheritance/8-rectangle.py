#!/usr/bin/python3
"""This module contains class Rectangle (based on BaseGeometry)"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseException):
    """Rectangle class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
