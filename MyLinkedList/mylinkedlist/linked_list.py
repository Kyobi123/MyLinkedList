from .node import Node

class LinkedList:
    """Implementación básica de una Linked List."""

    def __init__(self):
        self.head = None

    def append(self, data):
        """Agrega un nuevo nodo al final."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """Agrega un nuevo nodo al inicio."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Elimina el primer nodo con el valor dado."""
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:
            current.next = current.next.next

    def find(self, data):
        """Busca un nodo por valor."""
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __repr__(self):
        return " -> ".join(str(data) for data in self)