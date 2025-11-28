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

    def to_json(self):
        """This function retrieves a dictionary
         representation of a Student instance"""
        return self.__dict__
