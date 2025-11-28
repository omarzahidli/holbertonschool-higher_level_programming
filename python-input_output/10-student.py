#!/usr/bin/python3
"""
This module for Student to JSON task
"""


class Student:
    """This class about Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This function retrieves a dictionary
         representation of a Student instance"""
        if attrs is not None:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__
