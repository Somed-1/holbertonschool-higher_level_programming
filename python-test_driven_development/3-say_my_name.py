#!/usr/bin/python3
"""It's time cook."""


def say_my_name(first_name, last_name=""):
    """
    say_my_name - Wolter White? You're goddamn right.
    Args:
        first_name: first_name
        last_name: last_name
    Return:
        98.9 % poor meth
    """
    if not isinstance(first_name, (str)):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, (str)):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
