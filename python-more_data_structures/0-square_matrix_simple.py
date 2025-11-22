#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """Returns a new matrix with squares of all values in the input matrix."""
    return [[x ** 2 for x in row] for row in matrix]
