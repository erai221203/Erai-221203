a=[1,3,2,5]
b=len(a)

for i in a:
    if a[i]<a[i-1]:
        print(i)
    