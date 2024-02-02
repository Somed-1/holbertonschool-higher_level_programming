#!/usr/bin/python3
"""This module contains the function that prints text"""


def text_indentation(text):
    """
    text_indentation - prints text separated with 2 new lines

    Args:
    • text: text to print

    Return:
    • Nothing
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    ends = {".": ".\n\n", "?": "?\n\n", ":": ":\n\n"}
    ends_translation = str.maketrans(ends)
    text = text.translate(ends_translation)
    print("\n".join(line.strip() for line in text.split("\n")), end="")
