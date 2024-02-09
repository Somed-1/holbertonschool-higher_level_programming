#!/usr/bin/python3
"""This module contains function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """append_after function"""

    lines = []
    with open(filename, "r") as file:
        for line in file:
            line = line.replace(search_string, new_string)
            lines.append(line)

    with open(filename, "w") as file:
        file.writelines(lines)
