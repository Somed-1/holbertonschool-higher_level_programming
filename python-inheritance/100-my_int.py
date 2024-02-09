#!/usr/bin/python3
"""This module contains MyInt class"""


class MyInt(int):
    """MyInt class"""

    def __eq__(self, __value: object) -> bool:
        return not super().__eq__(__value)

    def __ne__(self, __value: object) -> bool:
        return not super().__ne__(__value)
