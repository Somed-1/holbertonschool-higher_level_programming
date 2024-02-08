#!/usr/bin/python3
"""This moduel contains read_file functoin"""


def read_file(filename=""):
    """read_file function"""

    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
