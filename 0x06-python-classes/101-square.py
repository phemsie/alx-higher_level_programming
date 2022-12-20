#!/usr/bin/python3
""" Square class with get set methods defined """


class Square:
    """ constructor method """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __repr__(self):
        newstr = ""
        if self.__size > 0:
            for row in range(self.__position[1]):
                newstr += "\n"
            for row in range(self.__size):
                for col in range(self.__position[0]):
                    newstr += " "
                for col in range(self.__size):
                    newstr += "#"
                newstr += "\n"
        else:
            newstr += '\n'
        return newstr[:-1]

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size > 0:
            for row in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for col in range(self.__position[0]):
                    print(" ", end="")
                for col in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
