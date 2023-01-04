#!/usr/bin/python3
""" module for a locked class """


class LockedClass:
    """ prevents the user from dynamically creating new instance
        attributes except by name first_name.
    """
    __slots__ = 'first_name'
