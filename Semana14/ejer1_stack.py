class Node:
  data: str

  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class Stack:
  head: Node
  
  def __init__(self,head):
    self.head = head
  
  def print_stack(self):
    current_node = self.head
    if current_node is None:
      print("Stack is empty")
      return None
    while current_node is not None:
        print(current_node.data)
        current_node = current_node.next

  def push_stack(self, new_node):
    new_node.next = self.head
    self.head = new_node
  

  def pop_stack(self):
    if self.head is None:
      print("Stack is empty. Cannot pop.")
      return None
    self.head = self.head.next
    return self.head

if __name__ == "__main__":
    node1 = Node("node1")
    node2 = Node("node2")
    node3 = Node("node3")
    
    stack = Stack(node1)
    stack.push_stack(node2)
    stack.push_stack(node3)
    
    print("Stack after pushing 3 nodes:")
    stack.print_stack()
    
    stack.pop_stack()
    print("\nStack after popping one node:")
    stack.print_stack()

    # Pop another node
    stack.pop_stack()
    print("\nStack after popping another node:")
    stack.print_stack()

    # Pop the last node
    stack.pop_stack()
    print("\nStack after popping the last node:")
    stack.print_stack()

    # Try to pop from an empty stack
    stack.pop_stack()