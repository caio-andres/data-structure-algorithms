class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def add_to_end(self, value):
        new_node = Node(value)
        new_node.prev = self.tail
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def remove_from_front(self):
        if not self.head:
            return None
        removed_value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return removed_value

    def remove_from_end(self):
        if not self.tail:
            return None
        removed_value = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return removed_value

    def to_list(self):
        """Retorna a lista como lista Python normal."""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

dll = DoublyLinkedList()

print("Lista inicial:", dll.to_list())

dll.add_to_front(10)
print("Após add_to_front(10):", dll.to_list())

dll.add_to_front(20)
print("Após add_to_front(20):", dll.to_list())

dll.add_to_end(5)
print("Após add_to_end(5):", dll.to_list())

removed = dll.remove_from_front()
print(f"Após remove_from_front() (removeu {removed}):", dll.to_list())

removed = dll.remove_from_end()
print(f"Após remove_from_end() (removeu {removed}):", dll.to_list())
