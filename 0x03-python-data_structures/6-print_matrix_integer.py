#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for m in matrix:
        i = 1
        for mem in m:
            if i != len(m):
                print("{:d}".format(mem), end=' ')
            else:
                print("{:d}".format(mem), end='')
            i += 1
        print()
