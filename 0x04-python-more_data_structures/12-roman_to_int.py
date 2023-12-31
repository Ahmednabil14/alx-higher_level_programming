#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
             "D": 500, "M": 1000}
    if roman_string is not str and roman_string is None:
        return 0
    for i in range(len(roman_string)):
        if roman[roman_string[i]] <= roman[roman_string[i - 1]] or i == 0:
            num += roman[roman_string[i]]
        else:
              num = num - roman[roman_string[i]]
    return num
