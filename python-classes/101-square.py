#!/usr/bin/python3
"""Define a class Square with properities"""


class Square:
    """Square class."""

    def __init__(self, size=0, position=(0, 0)) -> None:
        """__init__ method that sets the size of the square.
        Args:
            size (int): size of the square.
            position (tuple): position of square (x, y)
        """
        self.size = size
        self.position = position

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
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                print("{}{}".format(self.position[0] * " ", "#" * self.size))
        else:
            print()

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value


    def __str__(self):
        """
        __str__ - method to represent object as stirng
        Return:
            string that represents object
        """
        result = []
        if self.size > 0:
            for i in range(self.position[1]):
                result.append("")
            for i in range(self.size):
                result.append("{}{}".format(self.position[0] * " ", "#" * self.size))
        else:
            return "\n"

        return "\n".join(result)
