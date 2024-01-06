#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for x, num_value in enumerate(row):
            if x != 0:
                print(" ", end="")
            print("{:d}".format(num_value), end="")
        print()
