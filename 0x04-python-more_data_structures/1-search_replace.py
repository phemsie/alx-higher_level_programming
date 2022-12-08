#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [1 if l != search else replace for l in my_list]
