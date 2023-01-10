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

    def to_json(self, attrs=None):
        """
           If attrs is a list of strings, only attribute names
           contained in this list must be retrieved. Otherwise,
           all attributes must be retrieved
        """
        if attrs is None:
            return (self.__dict__)
        else:
            new = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new[key] = value
            return (new)
