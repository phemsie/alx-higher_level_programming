#!/usr/bin/python3
""" a module for a function that prints a square with the character #. """


def print_square(size):
    """ function that prints a square with the character #.
    Args:
        size: type int the size of the squares side
    Raises:
        TypeError: type of ize must be int
        ValueError: size must be > 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print(("#" * size + "\n") * size, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
