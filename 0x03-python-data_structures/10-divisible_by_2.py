#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    booll_list = []
    for i in my_list:
        if i % 2 == 0:
            booll_list.append(True)
        else:
            booll_list.append(False)
    return booll_list
