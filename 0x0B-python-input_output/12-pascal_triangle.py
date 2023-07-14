#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(size):
    """Represent Pascal's Triangle of given size.
    Returns a list of lists of integers representing the triangle.
    """
    if size <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != size:
        current_row = triangle[-1]
        next_row = [1]

        for i in range(len(current_row) - 1):
            next_value = current_row[i] + current_row[i + 1]
            next_row.append(next_value)

        next_row.append(1)
        triangle.append(next_row)

    return triangle
