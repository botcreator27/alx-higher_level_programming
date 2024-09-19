#!/usr/bin/python3

def roman_to_int(roman_string):
    i = 0
    result = 0  
    if type(roman_string) is not str or roman_string is None:
        return 0
    else:
        for string in roman_string:
            if string[i] == 'I':
                result += 1
            if string[i] == 'V':
                result += 5
            if string[i] == 'X':
                result += 10
            if string[i] == 'L':
                result += 50
            if string[i] == 'C':
                result += 100
            if string[i] == 'D':
                result += 500
            if string[i] == 'M':
                result += 1000
        return result
