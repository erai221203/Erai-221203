class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
    def display(self):
        if not self.head:
            print("Circular linked list is empty.")
            return
        current = self.head
        while True:
            print(current.data, end=' -> ')
            current = current.next
            if current == self.head:
                break
        print(self.head.data)
if __name__ == "__main__":
    cll = CircularLinkedList()
    for data in [1, 2, 3, 4]:
        cll.append(data)
    cll.display()
