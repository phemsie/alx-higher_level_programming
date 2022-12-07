#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    sum = 0
    total = 0
    for item in my_list:
        sum += (item[0] * item[1])
        total += item[1]
        return sum / total
