#!/usr/bin/python3
"""Student class definition."""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of a Student instance.

        If attrs is a list of strings, only return attributes listed.
        Otherwise, return all attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance.

        json is a dictionary where each key is an attribute name
        and each value is the value to assign.
        """
        for key, value in json.items():
            setattr(self, key, value)
