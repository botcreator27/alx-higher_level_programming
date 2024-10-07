#!/usr/bin/python3

"""This module defines a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    matrix_divided divides through the matrix by the value supplied.

    Args:
        matrix(list of lists of ints or float): the matrix
        div(int or float): the divisor

    Raises:
        TypeError: if matrix is not (list of lists) int or float
        TypeError: matrix not same size
        TypeError: div not a number
        ZeroDivisionError: div = 0

    Returns:
        the matrix with elements divided
    """
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if (not isinstance(matrix, list) or 
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) " +
                "of integers/floats")
    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists)" +
            "of integers/float")
    for x in row:
        if not isinstance(x, int) and not isinstance(x, float):
            raise TypeError("matrix must be a matrix (list of lists)"
            "of integers/float")

    len_rows = []
    for row in matrix:
        len_rows.append(len(row))
    if not all(x == len_rows[0] for x in len_rows):
        raise TypeError("Each row of matrix must have same size")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]
    return new_matrix
