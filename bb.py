a = [1, 0, 3, 4, 6, 5]

root = 1
left = []
right = []

for i in a:
    if i < root:
        left.append(i)
    else:
        right.append(i)

print("Left subtree:", left)
print("Right subtree:", right)
