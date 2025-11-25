#!/usr/bin/python3

"""module qui definit la classe Square"""


class Square:
    """class qui defini un carre"""

    def __init__(self, size=0):
        """initialise un carre avec une taille optionnel"""
        self.size = size

    def area(self):
        """fonction qui retourne l'aire du carre"""
        return self.__size * self.__size

    def __eq__(self, other):
        """
        Docstring for __eq__

        :param self: Description
        :param other: Description
        """

        return self.area() == other.area()

    def __ne__(self, other):
        """
        Docstring for __ne__

        :param self: Description
        :param other: Description
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Docstring for __lt__

        :param self: Description
        :param other: Description
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Docstring for __le__

        :param self: Description
        :param other: Description
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Docstring for __gt__

        :param self: Description
        :param other: Description
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Docstring for __ge__

        :param self: Description
        :param other: Description
        """
        return self.area() >= other.area()

    @property
    def size(self):
        """
        Docstring for size

        :param self: Description
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Docstring for size

        :param self: Description
        :param value: Description
        """

        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
