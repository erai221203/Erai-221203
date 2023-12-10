def organize_subtrees(root, elements):
    left = []
    right = []

    for i in elements:
        if i < root:
            left.append(i)
        else:
            right.append(i)

    print(f"Node {root}: Left subtree: {left}, Right subtree: {right}")

    if left:
        organize_subtrees(left[0], left[1:])
    if right:
        organize_subtrees(right[0], right[1:])
def search(g):
    for i in a:
        if i==g:
            None
            print('value detected at the index of',a.index(g))
        else:
            None
            
            print('Enter the correct value')
def maxi(a):
    c=max(a)
    print(c)
a = [1, 0, 3, 4, 6, 5,-10,100]

b=organize_subtrees(a[0], a[1:])
maxi(a)
search(0)

