
Sign up
AgeseVictor
/
alx-higher_level_programming
Public
Code
Issues
Pull requests
Actions
Projects
Security
Insights
alx-higher_level_programming/0x0B-python-input_output/7-add_item.py
@AgeseVictor
AgeseVictor help
 1 contributor
Executable File  20 lines (16 sloc)  497 Bytes
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
