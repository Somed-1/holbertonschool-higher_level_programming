#!/usr/bin/python3
"""This module contains class MyList"""


class MyList(list):
    """MyList class"""
    def print_sorted(self):
        """print_sorted method"""
        print(sorted(self))
