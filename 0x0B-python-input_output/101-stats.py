#!/usr/bin/python3
"""script that reads stdin line by line and computes stats metrics"""
import sys


def print_stats(file_size, dict):
    """prints statistics since beginning"""
    print("File size: {}".format(file_size))
    for key in dict:
        if dict[key] != 0:
            print("{}: {}".format(key, dict[key]))


"""declaring variables"""
file_size = 0
count = 0
dict = {'200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0}

""" Read from stdin """
try:
    for line in sys.stdin:
        if count == 10:
            print_stats(file_size, dict)
            count = 1
        else:
            count += 1

        line_split = line.split()
        file_size += int(line_split[-1])

        try:
            if line_split[-2] in dict:
                dict[line_split[-2]] += 1
        except IndexError:
            pass

    print_stats(file_size, dict)
except KeyboardInterrupt:
    print_stats(file_size, dict)
    raise
