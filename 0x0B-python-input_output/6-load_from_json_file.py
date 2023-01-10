#!/usr/bin/python3
""" module defines load_from_json_file method """


import json


def load_from_json_file(filename):
    """ creates an Object from a 'JSON file':
    args:
        filename: json file
    """
    text = ""
    with open(filename, mode="r", encoding="utf-8") as f:
        for line in f:
            text += line
        return json.loads(text)
