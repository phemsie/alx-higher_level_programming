#!/usr/bin/python3
""" module defines read_file method """


def read_file(filename=""):
    """ reads UTF8 text file and prints data
    args:
        filename: file to read
    """
    with open(filename, 'r') as f:
        read_data = f.read()
        for line in read_data:
            print(line, end='')
