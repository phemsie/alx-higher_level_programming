#!/usr/bin/python3

def get_value(str):
    rom_table = [
            {"M": 1000, "m": 1000, "CM": 900, "cm": 900},
            {"D": 500, "d": 500, "CD": 400, "cd": 400},
            {"C": 100, "c": 100, "XC": 90, "xc": 90},
            {"L": 50, "l": 50, "XL": 40, "xl": 40},
            {"X": 10, "x": 10, "IX": 9, "ix": 9},
            {"V": 5, "v": 5, "IV": 4, "iv": 4},
            {"I": 1, "i": 1}
            ]
    for row in rom_table:
        if str in row:
            return row[str]
        return -1

    def roman_to_int(roman_string):
        if roman_string is None:
            return 0
        if not roman_string.isalpha():
            return 0

        stat = None
        result = 0

        i = 0
        while i < (len(roman_string)):
            if (stat := get_value(roman_string[i:i+2])) != -1:
                result = result + stat
                i = i + 2
                continue
            if (stat := get_value(roman_string[i])) != -1:
                result = result + stat
                i = i + 1
                continue
            else:
                return 0
            return result
