#!/usr/bin/python3
"""a square class"""


class Square():
    """a class constructor"""

    def __init__(self, size=0):
        """validate size"""

        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calculates area"""

        return self.__size ** 2
