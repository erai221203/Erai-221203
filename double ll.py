class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
    def display_forward(self):
        if not self.head:
            print("Doubly linked list is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=' <-> ')
            current = current.next
        print("None")
    def display_backward(self):
        if not self.head:
            print("Doubly linked list is empty.")
            return
        current = self.head
        while current.next:
            current = current.next
        while current:
            print(current.data, end=' <-> ')
            current = current.prev
        print("None")
if __name__ == "__main__":
    dll = DoublyLinkedList()
    for data in [1, 2, 3, 4]:
        dll.append(data)
    print("Doubly linked list in forward direction:")
    dll.display_forward()
    print("Doubly linked list in backward direction:")
    dll.display_backward()