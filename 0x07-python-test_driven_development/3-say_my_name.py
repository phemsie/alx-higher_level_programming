#!/usr/bin/python3
""" a module for a function that prints My name is <first name> <last name> """


def say_my_name(first_name, last_name=""):
    """ function to prints My name is <first name> <last name
    Args:
        first_name: type str first name
        last_name: type str last name
    Raises:
        TypeError: first_name or last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
