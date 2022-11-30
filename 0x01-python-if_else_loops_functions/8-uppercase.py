#!/usr/bin/python3

def uppercase(str):
    for let in str:
        asc = ord(let)
        if asc in range(ord('a'), ord('z') + 1):
            asc = asc - 32
            print("{}".format(chr(asc)), end='')
            print()
