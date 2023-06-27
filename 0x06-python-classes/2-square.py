#!/usr/bin/python3

'''Defining a class square'''


class Square:
    '''Validating the type of private instance'''

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square to validate
        """
        if size is None:
            self.__size = None
        else:
            self.__size = size

        if not isinstance(self.__size, int):
            raise TypeError('size must be an integer')
        elif self.__size < 0:
            raise ValueError('size must be >= 0')
