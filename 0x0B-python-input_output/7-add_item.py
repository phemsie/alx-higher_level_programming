#!/usr/bin/python3
"""
script adds all arguments to a Python list, and then save them to a file
"""


from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
MyList = argv[1:]
try:
    my_obj = load_from_json_file(filename)
    my_obj += MyList
    save_to_json_file(my_obj, filename)
except:
    my_obj = MyList
    save_to_json_file(my_obj, filename)
