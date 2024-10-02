#!/usr/bin/python3
""" build a Class Node with me """


class Node:
    """ this class defines the node of a singly linked list

        Attributes:
        __data: stores value of node
        __next_node: node
    """
    def __init__(self, data, next_node=None):
        """ Initialises the class node
        Args:
            data(int): the value of the node
            next_node(node): node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ (int): this is the getter method for data """
        return self.__data

    @data.setter
    def data(self, value):
        """ setter method for data

        Args:
            value(int): the data field of node
        Raises:
            TypeError: data must be an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def new_node(self):
        """(node or None): the next node in the singly list """
        return self.__new_node

    @new_node.setter
    def new_node(self, value):
        """
        setter method for new_node

        Args:
            value(node or None): next node of a node
        Raises:
            TypeError: if new_node not of type node or none
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__new_node == value

class SinglyLinkedList:
    """Defines a singly linked list

    Attributes:
        __head: the head
        
    """
    def __init__(self):
        """ creates new instances of SinglyLinkedList

        Args:
            head: head of the class
        """
        self.__head = None

    def __str__(self):
        """Defines the string repersentation of the list

        Returns:
            str: string representation of the list, one node data per line
        """
        node = self.__head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """ inserts node at correct sorted position

        Args:
            value(int): value
        """
        new_node = Node(value)

        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
