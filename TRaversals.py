class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.key = k
def preorder(root):
    if root is not None:
        print(root.key)
        preorder(root.left)
        preorder(root.right)
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)
def postorder(root):
    if root is not None:
        inorder(root.left)
        
        inorder(root.right)
        print(root.key)
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
preorder(root)
print('\n\n')
inorder(root)
print('\n\n')
postorder(root)