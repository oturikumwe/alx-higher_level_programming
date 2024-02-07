#!/usr/bin/python3


class Node:
    """Represents a node of a singly linked list."""
    
    def __init__(self, data, next_node=None):
        """Initializes a new Node instance.
        Args:
        data (int): The data to be stored in the node.
        next_node (Node, optional): The next node in the list. Defaults to None.
        Raises:
        TypeError: If data is not an integer or next_node is not a Node object or None.
        """
        self.data = data
        self.next_node = next_node
    
    @property
    def data(self):
        """Getter method for retrieving the data of the node."""
        return self.__data
    
    @data.setter
    def data(self, value):
        """Setter method for setting the data of the node.
        Args:
        value (int): The data to be set.
        Raises:
        TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
    
    @property
    def next_node(self):
        """Getter method for retrieving the next node."""
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        """Setter method for setting the next node.
        Args:
        value (Node): The next node to be set.
        Raises:
        TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""
    
    def __init__(self):
        """Initializes a new SinglyLinkedList instance with an empty list."""
        self.head = None
    
    def sorted_insert(self, value):
    """Inserts a new Node into the correct sorted position in the list (increasing order).
    Args:
    value (int): The value to be inserted.
    """
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
    
    def __str__(self):
        """Returns a string representation of the entire list."""
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)
