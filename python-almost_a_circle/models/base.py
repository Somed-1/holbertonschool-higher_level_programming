#!/usr/bin/python3
"""This module contains class Base"""


class Base:
    """class Base"""

    __nb_objects = 0
    def __init__(self, id=None) -> None:
        if id is None:
            self.increase_nb()
            self.id = self.__nb_objects
        else:
            self.id = id

    @classmethod
    def increase_nb(cls):
        cls.__nb_objects += 1


if __name__ == "__main__":
    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
