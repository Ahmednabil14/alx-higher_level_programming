#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    i = 0
    for j in my_list:
        if j == search:
            new[i] = replace
        i += 1
    return new
