#!/usr/bin/python3
"""
A function that prints a square
with the character #.
"""


def print_square(size):
    """
    """
    if not isinstance(size, int) or isinstance(size, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for col in range(size):
            print("#", end="")
        print()
