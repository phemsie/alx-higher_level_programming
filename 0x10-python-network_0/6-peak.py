#!/usr/bin/python3
""" function find_peak """


def find_peak(list_of_integers):
    '''finds peak'''
    if len(list_of_integers) > 0:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None

