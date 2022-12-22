#!/usr/bin/python3
""" a module contains add_integer function
    b = 89 by default at least one arg is required
    raises a TypeError if a, b are not integers or float
    a, b will be casted to integers if they are float
"""


def add_integer(a, b=98):
    """ a function that adds 2 integers.
    casts type of a, b to int
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    """ returns an integer sum of a + b """
    return a + b
