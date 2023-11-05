#!/usr/bin/python3
def max_integer(my_list=[]):
    x = 0
    if len(my_list) != 0:
        my_list.sort()
        return my_list[-1]
    else:
        return None
