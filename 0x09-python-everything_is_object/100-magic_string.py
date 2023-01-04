#!/usr/bin/python3
def magic_string():
    setattr(magic_string, "z", getattr(magic_string, "z", -1) + 1)
    return "Holberton" + ", Holberton" * getattr(magic_string, "z", 0)
