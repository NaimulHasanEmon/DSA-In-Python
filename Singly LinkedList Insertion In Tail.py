class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next
  
  def __str__(self):
    return str(self.value)

head = Node(1)
a = Node(2)
b = Node(3)
c = Node(4)

head.next = a
a.next = b
b.next = c

def print_list(head):
  curr = head
  elements = []
  while curr:
    elements.append(str(curr.value))
    curr = curr.next
  
  print(" -> ".join(elements))

def insert_at_tail(head, value):
    new_node = Node(value)
    
    if head is None:
        head = new_node
        return head
    
    curr = head
    while curr.next:
        curr = curr.next
    
    curr.next = new_node
    return head

print_list(head)          # Output: 1 -> 2 -> 3 -> 4

head = insert_at_tail(head, 5)
print_list(head)          # Output: 1 -> 2 -> 3 -> 4 -> 5