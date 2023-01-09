#!/usr/bin/python3
"""module defined MyInt is a rebel."""


class MyInt(int):
    """class MyInt defined"""

    def __eq__(self, next):
        """eq inverted to ne"""
        return super().__ne__(next)

    def __ne__(self, next):
        """ne inverted to eq"""
        return super().__eq__(next)
