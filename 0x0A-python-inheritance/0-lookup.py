#!/usr/bin/python3
"""A function that returns a list"""

def lookup(obj):
    """
    a function that returns the list of available attributes
    and methods of an object:

    Args:
        obj(instance of class): the object

    Return:
        returns the list of available attributes and
        methods of an object:
    """
    return dir( obj)
