#!/usr/bin/python3
"""
This module contains:
    Class Node, which is element for singly linked list
    Class SinglyLinkedList, that implements singly linked list
"""


class Node:
    """Node class, an element of singly linked list"""
    def __init__(self, data, next_node=None):
        """
        __init__ - method to inicialize the instance of Node
        Args:
            data: value that node stores (int)
            next_node: pointer to the next node of the list
        Return:
            None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, (int)):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, (Node)) and value:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __str__(self):
        """
        __str__ - method that is used for stdout
        Return:
            A string that represents the object
        """
        return "{:d}".format(self.data)


class SinglyLinkedList:
    """SinglyLinkedList calss, implements singly linked list"""
    def __init__(self):
        """
        __init__ - method to inicialize the instance of Node
        Return:
            None
        """
        self.head = None

    def sorted_insert(self, value):
        """
        sorted_insert - inserts a Node to linked list in increasing order
        Args:
            value: a Node to insert
        Return:
            None
        """
        value = Node(value)
        cur = self.head

        if cur is None:
            self.head = value
            return

        if value.data <= cur.data:
            self.head = value
            value.next_node = cur
            return

        while cur.next_node:
            if value.data <= cur.next_node.data:
                value.next_node, cur.next_node = cur.next_node, value
                return
            cur = cur.next_node

        value.next_node, cur.next_node = cur.next_node, value

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, value):
        if not isinstance(value, (Node)) and value:
            raise TypeError("head must be a Node object")
        self.__head = value

    def __str__(self) -> str:
        """
        __str__ - method that is used for stdout
        Return:
            A string that represents the object
        """
        nodes = []
        cur = self.head
        while cur:
            nodes.append(cur)
            cur = cur.next_node
        return "\n".join(str(node) for node in nodes)
