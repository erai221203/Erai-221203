a=[1,2,3,4,[5,6,7,8],9,[10,11,[12,13]]]
class tree:
    def add(self,m,n,x,y):
        b=a[m]
        b.append(n)
        c=b[x]
        c.append(y)
        print('b',b)
        print(a)
        
    def pop(self,l):
        
       a[l].pop() 
       print(a)
    
o=tree()

o.add(6,45,2,1)

