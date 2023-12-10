#Stack operations
print('******Stack******')
l=[1,2,3,4,5]
class Stack:
    def Push(self,a):
        l.append(a)
        print(a,'is added to the list l:',l)
    def Pop(self):
        l.pop()
        print('Poped list:',l)
o=Stack()
o.Push(6)
o.Pop() 
print('\t') 