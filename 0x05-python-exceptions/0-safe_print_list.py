#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    nb_print = 0
    while True:
        try:
            if nb_print < x:
                print(my_list[nb_print], end='')
                nb_print += 1
            else:
                print()
                return nb_print
        except IndexError:
            print()
            return nb_print
