#!/usr/bin/python3
"""a square class"""


class Square():
    """a class constructor"""

    def __init__(self, size=0):
        """private attribute"""

        self.__size = size

    def area(self):
        """calculates area"""

        return self.__size ** 2

    @property
    def size(self):
        """getter method property decorator"""

        return self.__size

    @size.setter
    def size(self, value):
        """setter method validate value"""

        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
