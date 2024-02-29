#!/usr/bin/python3
"""program to get peak number"""


def find_peak(list_of_integers):
    """get the peak number"""
    if not list_of_integers:
        return None

    return find_peak_recursive(list_of_integers, 0, len(list_of_integers) - 1)


def find_peak_recursive(lst, first, last):
    """function to recursive"""
    if first == last:
        return lst[first]

    mid = (first + last) // 2

    if lst[mid] < lst[mid + 1]:
        return find_peak_recursive(lst, mid + 1, last)
    else:
        return find_peak_recursive(lst, first, mid)
