from typing import Optional

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next: Optional['Node'] = None

class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def append(self, value: int):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def __str__(self) -> str:
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return '[' + ', '.join(values) + ']'

def intercambiar_nodos_pares(linked_list: LinkedList) -> LinkedList:
    dummy = Node(0)
    dummy.next = linked_list.head
    prev = dummy
    curr = linked_list.head

    while curr and curr.next:
        first = curr
        second = curr.next

        prev.next = second
        first.next = second.next
        second.next = first

        prev = first
        curr = first.next

    return dummy.next

# Ejemplo de uso
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

new_head = intercambiar_nodos_pares(linked_list)
print(new_head)