#!/usr/bin/python3

"""module qui definit la classe Square"""


class Square:
    """class qui defini un carre"""

    def __init__(self, size=0, position=(0, 0)):
        """initialise un carre avec une taille optionnel"""
        self.size = size
        self.position = position

    def __str__(self):
        """fonction qui retourne la representation
        du carre en # sous forme de liste"""

        lines = []

        if self.size == 0:
            return ""

        for i in range(self.position[1]):
            lines.append("")

        for i in range(self.size):
            line = " " * self.position[0] + "#" * self.size
            lines.append(line)

        return "\n".join(lines)

    def area(self):
        """fonction qui retourne l'aire du carre"""

        return self.__size * self.__size

    @property
    def position(self):
        """affiche l'attribue priver position"""

        return self.__position

    @property
    def size(self):
        """affiche l'attribue priver size"""

        return self.__size

    @position.setter
    def position(self, value):
        """setter qui verifie avant de cree position"""

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        if not len(value) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    @size.setter
    def size(self, value):
        """setter qui verifie avant de cree size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """retourne la representation du carre avec des #"""
        if self.size == 0:
            print("")
            return

        for i in range(self.position[1]):
            print()

        for i in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
