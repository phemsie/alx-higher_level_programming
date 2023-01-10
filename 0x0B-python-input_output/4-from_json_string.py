#!/usr/bin/python3
""" module defines from_json_string method """


import json


def from_json_string(my_str):
    """ returns an obj for JSON string repr
    args:
        my_str: a json object
    """
    return json.loads(my_str)
