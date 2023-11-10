#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    add = 0
    for x in my_list:
        if x not in new:
            new.append(x)
    for i in new:
        add += i
    return add
