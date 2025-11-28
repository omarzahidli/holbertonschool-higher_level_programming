#!/usr/bin/python3
"""
This module provides a function to check if
an object is an instance of a class or its subclasses.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if obj is an instance of a_class or a subclass of a_class.

    Args:
        obj: The object to check.
        a_class: The class or superclass to compare against.

    Returns:
        True if obj is an instance of a_class or its subclass, False otherwise.
    """
    return isinstance(obj, a_class)
