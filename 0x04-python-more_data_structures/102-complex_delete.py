#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    lis = []
    for key, val in a_dictionary.items():
        if val == value:
            lis.append(key)
    for i in lis:
        del a_dictionary[i]
    return a_dictionary
