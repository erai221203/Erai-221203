def merge(a):
    if len(a)>1:
        mid=len(a)//2

        left=a[:mid]
        right=a[mid:]

        merge(left)
        merge(right)
        
        a.clear()
        while len(left) and len(right)>0:
            if left[0]<=right[0]:
                a.append(left[0])
                left.pop(0)
            else:
                a.append(right[0])
                right.pop(0)
        
        for i in left:
            a.append(i)
        for j in right:
            a.append(j)
    
a=[4,1,3,9,7]
merge(a)
print(a)