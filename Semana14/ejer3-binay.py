from ejer1_stack import Stack

class Node:
    data: str
    
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.left = next
        self.right = prev


class NodeStack:
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
        current_node = current_node.right

  def push_stack(self, new_node):
    new_node.right = self.head
    self.head = new_node
  

  def pop_stack(self):
    if self.head is None:
      print("Stack is empty. Cannot pop.")
      return None
    popped = self.head
    self.head = self.head.right
    return popped


class BinaryTree:
    root: Node

    def __init__(self, root):
        self.root = root
        self.node_count = 1

    def print_tree(self):
        current = self.root
        stack = Stack(None)
        i = 0
        direction = ''
        aux = 0
        while current is not None or stack.head is not None:
            #Left
            while current is not None:
                stack.push_stack(Node(current))
                current = current.left
                direction = 'left'
            
            node_stack = stack.pop_stack()
            current = node_stack.data
            if i != 0:
                print(f'{direction}: {current.data}')
            else:
                print(f'Root: {current.data}')
            #Right
            current = current.right
            direction = 'right'
            i += 1

   
    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    self.node_count += 1
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    self.node_count += 1
                    return
                current = current.right
    
if __name__ == "__main__":
    root_node = Node("m")
    tree = BinaryTree(root_node)
    
    tree.insert("b")
    tree.insert("r")
    tree.insert("a")
    tree.insert("c")
    tree.insert("q")
    tree.insert("z")
    
    print("In-order of the binary tree:")
    tree.print_tree()