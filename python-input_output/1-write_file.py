#!/usr/bin/python3
"""This module contains function write_file"""


def write_file(filename="", text=""):
    """write_file function"""

    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
