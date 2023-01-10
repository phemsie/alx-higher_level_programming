#!/usr/bin/python3
""" module defines class_to_json method """


def class_to_json(obj):
    """ returns the dictionary description
    with simple data structure
    args:
        obj: is an instance of a Class
    """
    return (obj.__dict__)
