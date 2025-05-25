class SinglyLinkedList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def __str__(self):
        return str(self.value)

head = SinglyLinkedList(1)
A = SinglyLinkedList(2)
B = SinglyLinkedList(3)
C = SinglyLinkedList(4)

head.next = A
A.next = B
B.next = C

# print(head)

def print_linked_list(head):
    curr = head
    elements = []
    
    while curr:
        elements.append(str(curr))
        curr = curr.next
    
    print(" -> ".join(elements))

# print_linked_list(head)

def search_linked_list(head, target):
    curr = head
    
    while curr:
        if curr.value == target:
            return True
        curr = curr.next
    return False

# print(search_linked_list(head, 7))

class DoublyLindedList:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return str(self.value)

head = DoublyLindedList(1)
A = DoublyLindedList(2)
B = DoublyLindedList(3)
C = DoublyLindedList(4)
D = DoublyLindedList(5)
head.next = A
head.prev = None
A.next = B
A.prev = head
B.next = C
B.prev = A
C.next = D
C.prev = B
D.next = None
D.prev = C

# print(head)

def print_doubly_linked_list(head):
    curr = head
    elements = []
    
    while curr:
        elements.append(str(curr))
        curr = curr.next
    
    print(" <-> ".join(elements))

print_doubly_linked_list(head)