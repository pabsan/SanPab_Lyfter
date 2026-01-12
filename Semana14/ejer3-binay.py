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

    def print_in_order(self):
        stack = []
        current = self.root
        level_count = 0
        count_nodes = self.node_count
        i = 0

        while current is not None or stack:
            # Go to the leftmost node
            while current is not None:
                stack.append(current)
                current = current.left
                flag = '/'  # Just to indicate direction

            # Visit node
            current = stack.pop()
            i += 1
            if i > 2:
                level_count += 1
                i = 0
            node_print = current.data
            if i == 1:
                print(f'{node_print.rjust(count_nodes)} \n{flag.rjust(count_nodes)}')
            else:
                print(f'{node_print.rjust(count_nodes)} \n{flag.rjust(count_nodes)}')
            count_nodes -= 1
            # Go to the right node
            current = current.right
            flag = '\\'  # Just to indicate direction
    
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
    tree.print_in_order()