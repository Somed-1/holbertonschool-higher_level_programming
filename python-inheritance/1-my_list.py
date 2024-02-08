#!/usr/bin/python3
"""This module contains class MyList"""


class MyList(list):
    """MyList class"""
    def print_sorted(self):
        """print_sorted method"""
        new_list = sorted(self)
        print(new_list)
        return new_list
