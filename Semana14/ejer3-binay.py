class Node:
    data: str
    
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.left = next
        self.right = prev


class BinaryTree:
    root: Node

    def __init__(self, root):
        self.root = root
        self.node_count = 1
    

    def format_output(self, node, is_root):
       if is_root:
          return f'Root: {node.data}'
       else:
          return f'{node.data}'
    

    def print_node(self,text):
        print(text)

    def print_tree(self):
        current = self.root
        #stack = Stack(None)
        i = 0
        direction = ''
        first = True
        aux = None
        while current is not None or aux is not None:
            #Left
            while current is not None:
                temp_left = current.left

                #push to aux
                current.left = aux
                aux = current

                current = temp_left

            node = aux
            aux = aux.left
            node.left = None

            if first:
               first = False
               text = self.format_output(node, True)
               self.print_node(text)
            else:
                text = self.format_output(node, False)
                self.print_node(text)
            
            current = node.right

   
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