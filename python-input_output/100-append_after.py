#!/usr/bin/python3
"""This module contains function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """append_after function"""

    lines = []
    with open(filename, "r") as file:
        for line in file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, "w") as file:
        file.writelines(lines)
