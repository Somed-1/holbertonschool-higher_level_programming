#!/usr/bin/python3
"""Define a class Square with properities"""


class Square:
    """Square class."""

    def __init__(self, size=0) -> None:
        """__init__ method that sets the size of the square.
        Args:
            size (int): size of the square.
        """
        self.size = size

    def area(self):
        """Public instance method that returns the
        current square area.area method that returns the area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Public instance method that pritns the current square.
        """
        if self.size > 0:
            for i in range(self.size):
                print("{}".format("#" * self.size))

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
