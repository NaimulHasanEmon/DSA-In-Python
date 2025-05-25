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

def delete_by_index(head, index):
    if head is None:
        print("List is empty.")
        return head

    if index < 0:
        print("Index cannot be negative.")
        return head
    
    if index == 0:
        return head.next
    
    curr = head
    current_index = 0
    
    while curr and curr.next:
        if current_index == index - 1:
            curr.next = curr.next.next
            return head
        
        curr = curr.next
        current_index += 1

print_list(head)          # Output: 1 -> 2 -> 3 -> 4

head = delete_by_index(head, 1)
print_list(head)          # Output: 1 -> 3 -> 4