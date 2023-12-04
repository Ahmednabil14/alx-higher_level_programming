#!/usr/bin/python3
"""
program that prints the list, but sorted (ascending sort)
"""


class MyList(list):
    """
    class MyList that inherit from list class
    """

    def print_sorted(self):
        """
        function that prints the list, but sorted (ascending sort)
        """

        print(sorted(self))
