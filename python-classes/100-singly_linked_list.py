#!/usr/bin/python3
"""module qui defini la class Node et SinglyLinkedList"""


class Node:
    """class qui defini un Node"""

    def __init__(self, data, next_node=None):
        """initialise un node avec data et next_node"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """affiche l'attribue priver data"""

        return self.__data

    @property
    def next_node(self):
        """affiche l'attribue priver next_node"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter pour l'instance next_node"""

        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value

    @data.setter
    def data(self, value):
        """setter pour l'instance data"""

        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value


class SinglyLinkedList:
    """class qui defini SinglyLinkedList"""

    def __init__(self):
        """initialise une liste"""

        self.__head = None

    def sorted_insert(self, value):

        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
            return

        if value <= self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head

        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
