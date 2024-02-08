#!/usr/bin/python3
"""This moduel contains read_file functoin"""


def read_file(filename=""):
    """read_file function"""
    with open(1, "w") as stdout:
        with open(filename, "r", encoding="utf-8") as file:
            stdout.write(file.read())
