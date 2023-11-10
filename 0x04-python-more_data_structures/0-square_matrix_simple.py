#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = []
    for x in matrix:
        newrow = []
        for y in x:
            newrow.append(y ** 2)
        newmatrix.append(newrow)
    return newmatrix
