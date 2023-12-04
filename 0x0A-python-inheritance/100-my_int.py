#!/usr/bin/python3
"""
equal operator
"""


class MyInt(int):
    """
    MyIny class that inherit from int class
    """

    def __eq__(self, object):
        """
        override operator
        """
        return super().__ne__(object)

    def __ne__(self, object):
        """
        override operator
        """
        return super().__eq__(object)
