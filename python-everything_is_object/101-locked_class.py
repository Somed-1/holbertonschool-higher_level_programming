#!/usr/bin/python3
"""This module contains LockedClass class"""


class LockedClass:
    """LockedClass class"""

    def __setattr__(self, __name, __value):
        """__setattr__ method"""

        if __name == "first_name":
            super().__setattr__(__name, __value)
        else:
            print(f"[AttributeError] 'LockedClass' object has no attribute '{__name}'")

    def __getattribute__(self, __name: str) -> Any:
        """__getattribute__ method"""

        if __name == "first_name":
            super().__getattribute__(__name)
        else:
            print(f"[AttributeError] 'LockedClass' object has no attribute '{__name}'")
