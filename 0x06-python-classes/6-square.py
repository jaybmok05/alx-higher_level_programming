#!/usr/bin/python3


'''Defining a class square'''


class Square:
    '''Validating the type of private instance'''

    def __init__(self, size=0, position=(0, 0)):
        """Defining method to return square area

        Args:
            size (int): The size of the new square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get/set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        self.__position = value

        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Method that returns an area of square"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the # character."""
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

        if self.__size == 0:
            print("")
            return
