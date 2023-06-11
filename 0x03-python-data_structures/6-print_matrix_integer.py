#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for outer_loop in matrix:
        for in_loop in outer_loop:
            print("{:d}".format(in_loop), end=' ')
        print()
