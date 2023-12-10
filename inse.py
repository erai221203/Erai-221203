def iss(ll):
    for i in range(1,len(ll)):
        k=ll[i]
        j=i-1
        while j>=0 and k< ll[j]:
               ll[j+1]=ll[j]
               j-=1
        ll[j+1]=k
        print(ll)
arr=[5,3,4,2]
iss(arr)