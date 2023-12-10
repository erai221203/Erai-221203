def qs(a):
    if len(a) > 1:
        pivot=a[-1]

        left=[]
        right=[]
    else:
        return a
    
    for i in a[:-1]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)
        
    return qs(left)+[pivot]+qs(right)

a=[4,1,3,9,7]
b=qs(a)
print(b)
