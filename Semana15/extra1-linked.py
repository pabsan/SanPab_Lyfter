class Node:
  data: str
  next: "Node"

  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class LinkedList:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head

        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next


def my_buble_sort(myLinkedList):
    modified = True
    while modified:
        current = myLinkedList.head
        modified = False

        while current.next is not None:
            if current.data > current.next.data:
                temp = current.data
                current.data = current.next.data
                current.next.data = temp
                modified = True
            current = current.next
    


third_node = Node("b")
second_node = Node("c", third_node)
first_node = Node("a", second_node)

linked_list = LinkedList(first_node)
print("Unsorted:")
linked_list.print_structure()

print("Sorted:")
my_buble_sort(linked_list)
linked_list.print_structure()


sor1ted_list = LinkedList(Node(1, Node(2, Node(3))))
print("Unsorted:")
sor1ted_list.print_structure()
print("Sorted:")
my_buble_sort(sor1ted_list)
sor1ted_list.print_structure()

other_list = LinkedList(Node(5000, Node(70, Node(10, Node(100)))))
print("Unsorted:")
other_list.print_structure()
print("Sorted:")
my_buble_sort(other_list)
other_list.print_structure()