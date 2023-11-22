#!/usr/bin/python3
"""
defining single list
"""


class Node:
    def __init__(self, data, next_node=None):
        """
        instance of the class
        arguments:
            data: data in the list
            next_node: the next node in the list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        getter property
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        setter property
        arguments:
            value: the new data
        exceptions:
            TypeError: if value is not int
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        getter property
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        setter property
        arguments:
            value: the new value
        exceptions:
            TypeError: if it is not node
        """
        if not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        """
        new instance
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        add a node to the list
        arguments:
            value: the value to be inserted
        """
