#!/usr/bin/python3
""" MagicClass """
import math


class MagicClass:
    """ Magic instance """
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    """ Calculates area """
    def area(self):
        return self.__radius ** 2 * math.pi

    """ Calculates circumference """
    def circumference(self):
        return 2 * math.pi * self.__radius
