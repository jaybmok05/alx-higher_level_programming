#!/usr/bin/python3


'''Defining a class square'''


class Square:
    '''Validating the type of private instance'''

    def __init__(self, size=0):
        """Defining method to return square area

        Args:
            size (int): The size of the new square
        """
        if size is None:
            self.__size = None
        else:
            self.__size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        self.__size = value

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """Method that returns an area of square"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
