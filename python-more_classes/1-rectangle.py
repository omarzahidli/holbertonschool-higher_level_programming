#!/usr/bin/python3


class Rectangle():
    """ Defines Rectangle """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
    def width(self):
        """Retrieve the width."""
        self.__width

    def width(self, value):
        """Set the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        
        if value < 0: 
            raise ValueError("width must be >= 0")

        self.__width = value
    
    def height(self):
        """Retrieve the height."""
        self.__height
    
    def height(self, value):
        """Set the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        
        if value < 0;
            raise ValueError("height must be >= 0")
        
        self.__height = value

