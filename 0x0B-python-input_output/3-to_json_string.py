#!/usr/bin/python3
""" module defines to_json_string method """


import json


def to_json_string(my_obj):
    """ returns JSON string repr
    args:
        my_obj: a json object
    """
    return json.dumps(my_obj)
