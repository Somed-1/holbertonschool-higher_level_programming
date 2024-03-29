#!/usr/bin/python3
"""This module contains the function that devides elements of matrix"""


def matrix_divided(matrix, div):
    """
    devide_matrix - devides elements of matrix by given div
    Args:
        matrix: matrix to work with (Must contain only list with int, flaot)
        div: the number to use as div (int, float)
    Return:
        New matrix
    """
    tmessage = "matrix must be a matrix (list of lists) of integers/floats"
    smessage = "Each row of the matrix must have the same size"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0 or div == 0.0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, (list)):
        raise TypeError(tmessage)

    for row in matrix:

        if not all(isinstance(i, (int, float)) for i in row):
            raise TypeError(tmessage)

        if len(row) != len(matrix[0]):
            raise TypeError(smessage)

    return [[round(i / div, 2) for i in row] for row in matrix]
