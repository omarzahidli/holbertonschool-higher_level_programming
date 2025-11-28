#!/usr/bin/python3
"""Defines the MyList class that inherits from list."""


class MyList(list):
    """Custom list class with print_sorted and overridden methods."""

    def __init__(self):
        """Initialize the MyList object."""
        super().__init__()

    def append(self, item):
        """Append an item to the list."""
        super().append(item)

    def __str__(self):
        """Return the string representation of the list."""
        return super().__str__()

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
