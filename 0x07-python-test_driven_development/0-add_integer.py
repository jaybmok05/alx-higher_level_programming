#!/usr/bin/python3
"""A function that adds two integers"""


def add_integer(a, b=98):
    """Return sum addition of a and b.


    Float arguments are typecasted to ints before addition is performed.


    Args:
        a(ints/floats): the first value
        b(ints/floats): the second value


    Raises:
        TypeError: If neither a or b is a integer and float.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
