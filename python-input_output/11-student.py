#!/usr/bin/python3
"""Square module.

Contains a class Square that inherits from
Rectangle and some methods.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines the Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initializing for Square object"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Area calculator function"""
        return self.__size * self.__size

    def __str__(self):
        """Printing the Square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
