#!/usr/bin/python3
import pickle

"""
This module is for serializing and deserializing
custom Python objects using the pickle module.
"""

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except FileNotFoundError:
            print(f"File {filename} not found.")

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            print(f"File {filename} not found.")
            return None
        except Exception as e:
            print(f"Error during deserialization: {e}")
            return None
