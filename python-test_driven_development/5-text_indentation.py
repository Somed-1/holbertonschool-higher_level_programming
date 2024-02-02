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

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")
