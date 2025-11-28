#!/usr/bin/python3
"""Module containing empty class"""


class BaseGeometry:
    """Class for BaseGeometry"""
    def area(self):
        """Method to raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validate integer"""

        if type(value) is not int:
            raise TypeError(name + " must be an integer")

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
