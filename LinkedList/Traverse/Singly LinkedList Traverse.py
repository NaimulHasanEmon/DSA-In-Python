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

def traverse(head):
  curr = head
  elements = []
  while curr:
    elements.append(str(curr.value))
    curr = curr.next
  
  print(" -> ".join(elements))

traverse(head)        # Output: 1 -> 2 -> 3 -> 4