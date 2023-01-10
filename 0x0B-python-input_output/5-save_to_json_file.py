#!/usr/bin/python3
""" module defines save_to_json_file method """


import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file
    args:
        my_obj: a json object
        filename: file to save json obj
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
