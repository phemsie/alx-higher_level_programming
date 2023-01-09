#!/usr/bin/python3
"""
module that inherits list then calls sorted method
"""


class MyList(list):
    """class MyList inherits class list"""

    def print_sorted(self):
        print(sorted(self))
