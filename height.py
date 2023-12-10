class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.key = k

def treeSize(root):
    if root == None:
        return 0
    else:
        ls = treeSize(root.left)
        rs = treeSize(root.right)
        return max(ls , rs) + 1

# Creating a binary tree
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
root.right.right.left = Node(40)

# Calculating the size of the tree
size = treeSize(root)
print("Size of the tree:", size)
