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


p = Square(4)
print(p.size)
