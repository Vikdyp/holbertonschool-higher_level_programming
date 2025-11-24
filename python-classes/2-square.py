#!/usr/bin/python3

"""module qui definit la classe Square"""


class Square:
    """class qui defini un carre"""

    def __init__(self, size=0):
        """initialise un carre avec une taille optionnel"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
