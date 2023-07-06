#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle():
    """A class that defines private attributes"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >=0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >=0")

    @property
    def height(self):
        """Getter the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """setter the height of the rectangle."""
        self.__height = value

    @property
    def width(self):
        """Getter the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """setter the height of the rectangle."""
        self.__width = value
