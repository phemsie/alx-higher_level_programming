#!/usr/bin/python3

def remove_char_at(str, n):
    i = 0
    newStr = ""
    while i < len(str):
        if i != n:
            newStr += str[i]
            i += 1
            return newStr
