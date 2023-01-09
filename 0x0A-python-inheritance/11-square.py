#!/usr/bin/python3
""" module that defines a class Square that inherits from Rectangle """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square defined """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
        self.area()

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
