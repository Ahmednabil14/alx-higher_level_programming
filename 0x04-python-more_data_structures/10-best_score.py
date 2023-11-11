#!/usr/bin/python3
def best_score(a_dictionary):
    num = 0
    keey = ""
    if a_dictionary is not None:
        for key, val in a_dictionary.items():
            if val > num:
                num = val
                keey = key
        return keey
    else:
        return None
