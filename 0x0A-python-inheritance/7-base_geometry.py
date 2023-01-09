#!/usr/bin/python3
""" module that defines a class BaseGeometry """


class BaseGeometry:
    """ class BaseGeometry """

    def area(self):
        """ public method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value: is int and > 0 """
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")
