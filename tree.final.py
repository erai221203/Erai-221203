a=[1,2,3,4,[5,6,7,8],9,[10,11,[12,13]]]
class tree:
    def display(self):
        print('list',a)
    def search(self,x):
        b=a[x]
        print('Found:',b)
    def insertion(self,m,n,x,y):
        b=a[m]
        b.append(n)
        c=b[x]
        c.append(y)
        print('b:',b)
        print('a:',a)
        
    def deletion(self,l,n):
       a.pop(n) or a[l].pop(n) 
       print(a)


    
o=tree()
o.search(4)
