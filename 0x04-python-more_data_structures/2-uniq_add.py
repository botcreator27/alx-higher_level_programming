#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum = 0
    no_duplicate = set(my_list)
    for x in no_duplicate:
        sum += x

    return sum
