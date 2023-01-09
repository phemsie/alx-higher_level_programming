#!/usr/bin/python3
"""
Method compares obj is an instance of that inerited from class
"""


def inherits_from(obj, a_class):
    """ checks obj is an instance of a_class"""
    return isinstance(obj, a_class) and type(obj) != a_class
