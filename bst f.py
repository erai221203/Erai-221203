class Node:
    def __init__(self, key):
        self.left = self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)
        
    def _insert_recursive(self, root, key):
        if root is None:
            return Node(key)
        if key < root.val:
            root.left = self._insert_recursive(root.left, key)
        else:
            root.right = self._insert_recursive(root.right, key)
        return root

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)

    def in_order_traversal(self):
        return self._in_order_traversal_recursive(self.root)

    def _in_order_traversal_recursive(self, root):
        if root:
            yield from self._in_order_traversal_recursive(root.left)
            yield root.val
            yield from self._in_order_traversal_recursive(root.right)

# Example usage:
if __name__ == "__main__":
    bst = BinarySearchTree()
    for key in [50, 30, 20, 40, 70, 60, 80]:
        bst.insert(key)

    # In-order traversal (prints the sorted elements in ascending order)
    print("In-order traversal:", list(bst.in_order_traversal()))

    # Searching for a value
    result = bst.search(60)
    if result:
        print("Value found:", result.val)
    else:
        print("Value not found")
