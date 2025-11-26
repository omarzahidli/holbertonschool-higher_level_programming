#!/usr/bin/python3
""" Returns rectangle """

class Rectangle():
    """ Defines rectangle """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrieve the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width with validation. """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ Retrieve the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the width with validation. """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    @property
    def area(self):
        """ Return Area """
        return self.__width * self.__height

    @property
    def perimeter(self):
        """ Return Perimeter """
        return (self.__width * self.__height)+2
