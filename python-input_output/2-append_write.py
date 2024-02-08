#!/usr/bin/python3
"""This module contains append_write function"""


def append_write(filename="", text=""):
    """append_write funtion"""

    with open(filename, "a", encoding="utf-8") as file:
        file_len = file.write(text)

    return file_len
