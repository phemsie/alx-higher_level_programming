#!/usr/bin/python3
"""
This is the "Student"  class module
"""


class Student:
    """A class that defines a Student"""
    def __init__(self, first_name, last_name, age):
        """Student object instance constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation"""
        return (self.__dict__)
