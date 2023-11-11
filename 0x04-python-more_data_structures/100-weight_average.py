#!/usr/bin/python3
def weight_average(my_list=[]):
    total = 0
    sub = 0
    for ls in my_list:
        total += ls[0] * ls[1]
        sub += ls[1]
    avr = total / sub
    return avr
