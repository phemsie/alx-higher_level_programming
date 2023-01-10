#!/usr/bin/python3
""" module defines append_write method """


def append_write(filename="", text=""):
    """ appends a string to a file
    args:
        filename: file to write to
        text: string to append
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
