#!/usr/bin/python3
""" module defines write_file method """


def write_file(filename="", text=""):
    """ writes UTF8 text file
    args:
        filename: file to write to
        text: string to be written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
