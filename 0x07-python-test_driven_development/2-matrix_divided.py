#!/usr/bin/python3
"""
dividing a list of numbers
"""


def matrix_divided(matrix, div):
    """
    function that divide a list of list of intgers or float
    arguments:
        matrix: list of list of int or float
        div: the division number
    Return: the divided matrix
    Exceptions:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)\
                         of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    result = []
    for i in matrix:
        x = []
        if type(i) is not list:
            raise TypeError("matrix must be a matrix (list of lists)\
                             of integers/floats")
        if len(matrix[0]) != len(matrix[1]):
            raise TypeError("Each row of the matrix must have the same size")
        for n in i:
            if type(n) is not int and type(n) is not float:
                raise TypeError("matrix must be a matrix (list of lists)\
                                 of integers/floats")
            x.append(round(n / div, 2))
        result.append(x)
    return result
