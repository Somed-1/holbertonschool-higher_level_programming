#!/usr/bin/python3
"""This module contains LockedClass class"""


class LockedClass:
    """LockedClass class"""

    def __setattr__(self, __name, __value):
        """__setattr__ method"""

        if __name == "first_name":
            super().__setattr__(__name, __value)
        raise AttributeError(f"'LockedClass' object has no attribute '{__name}'")
