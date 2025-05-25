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

def search_by_value(head, value):
  curr = head
  current_index = 0
  
  while curr:
    if curr.value == value:
      return True, current_index
    
    curr = curr.next
    current_index += 1
  return False, None

print_list(head)          # Output: 1 -> 2 -> 3 -> 4

present, index = search_by_value(head, 3)

if present:
  print(f"Value found at index {index}.")

else:
  print("Value not found in the list.")