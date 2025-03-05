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

def sumar_dos_numeros(l1: LinkedList, l2: LinkedList) -> LinkedList:
    result = LinkedList()
    carry = 0
    current1 = l1.head
    current2 = l2.head

    while current1 or current2 or carry:
        val1 = current1.value if current1 else 0
        val2 = current2.value if current2 else 0
        temp_sum = val1 + val2 + carry
        carry = temp_sum // 10
        result.append(temp_sum % 10)

        if current1:
            current1 = current1.next
        if current2:
            current2 = current2.next

    return result


l1 = LinkedList()
l1.append(2)
l1.append(4)
l1.append(3)

l2 = LinkedList()
l2.append(5)
l2.append(6)
l2.append(4)

result = sumar_dos_numeros(l1, l2)
print(result)