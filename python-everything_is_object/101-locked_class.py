#!/usr/bin/python3
"""This module contains LockedClass class"""


class LockedClass:
    """LockedClass class"""

    def __setattr__(self, __name, __value):
        """__setattr__ method"""

        if __name == "first_name":
            super().__setattr__(__name, __value)
        else:
            text = f"'LockedClass' object has no attribute '{__name}'"
            raise AttributeError(text)

    def __getattribute__(self, __name):
        """__getattribute__ method"""

        if __name == "first_name":
            super().__getattribute__(__name)
        else:
            text = f"'LockedClass' object has no attribute '{__name}'"
            raise AttributeError(text)
