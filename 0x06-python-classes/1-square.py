#!/usr/bin/python3

'''Defining a square class'''


class Square:
    '''create a priveate instance attribute'''
    def __init__(self, size=None):
        if size is None:
            self.__size = None
        else:
            self.__size = size
