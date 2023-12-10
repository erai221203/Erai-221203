a=[1,2,3,4,[5,6,7,8],9,[10,11,[12,13]]]
class tree:
    def add(self,m,n):
        b=a[m]
        b.append(n)
        print(a)
    def pop(self,l):
        a.pop() or  a[l].pop()
       
        print(a)
    
o=tree()
o.pop(6)
