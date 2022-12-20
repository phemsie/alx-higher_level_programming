#!/usr/bin/python3
"""a square class"""


class Square():
    """a class constructor"""

    def __init__(self, size=0, position=(0, 0)):
        """private attribute"""

        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """position getter method property decorator"""

        return self.__position

    @position.setter
    def position(self, value):
        """setter method validate value"""

        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """prints a # square"""

        num = self.size
        line = self.position

        if num is 0:
            print("")
        else:
            for i in range(line[1]):
                print("")
            for j in range(num):
                for n in range(num + line[0]):
                    if n < line[0]:
                        print(" ", end='')
                    else:
                        print("#", end='')
                print("")
