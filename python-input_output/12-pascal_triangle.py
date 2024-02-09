#!/usr/bin/python3
"""This module contains function pascal_triangle"""


def pascal_triangle(n):
    """pascal_triangle function"""

    rows = [[1]]
    for j in range(n):
        above = [0] + rows[-1] + [0]
        row = [above[i] + above[i + 1] for i in range(len(above) - 1)]
        rows.append(row)

    return rows
