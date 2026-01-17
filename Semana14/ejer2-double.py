class Node:
    data: str
    
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleEndedQueue:
    head: Node
    tail: Node

    def __init__(self):
        self.head = None
        self.tail = None
    
    def push_left(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def push_right(self, new_node):
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def pop_left(self):
        if self.head is None:
            print("Deque is empty. Cannot pop from left.")
            return None
        popped_node = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        return popped_node
    
    def pop_right(self):
        if self.tail is None:
            print("Deque is empty. Cannot pop from right.")
            return None
        popped_node = self.tail
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        return popped_node
    
    def print_deque(self):
        current_node = self.head
        if current_node is None:
            print("Deque is empty")
            return
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


if __name__ == "__main__":
    deque = DoubleEndedQueue()
    
    node1 = Node("node1")
    node2 = Node("node2")
    node3 = Node("node3")
    node4 = Node("node4")
    
    deque.push_left(node1)
    deque.push_right(node2)
    deque.push_left(node3)
    deque.push_right(node4)
    
    print("Deque after pushing 4 nodes:")
    deque.print_deque()
    
    deque.pop_left()
    print("\nDeque after popping from left:")
    deque.print_deque()
    
    deque.pop_right()
    print("\nDeque after popping from right:")
    deque.print_deque()