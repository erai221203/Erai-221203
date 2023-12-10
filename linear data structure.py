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
#Queue
print('******Queue******')
l1=[1,2,3,4,5]
class Queue:
    def Enqueue(self,a):
        l1.append(a)
        print(a,'is added to the list l:',l)
    def Dequeue(self,a):
        l1.pop(0)
        print('Poped list:',l)
o=Queue()
o.Enqueue(0)
o.Dequeue(0)
print('\t') 
#Linked list
print('******Linked list******')
l2=[1,2,3,4,5,6]
class Linked:
    def Insertion(self,a,b):
        l2.insert(a,b)
        print(a,'is added to the list l:',l2)
    def Deletion(self,a):
        l2.pop(a)
        print('Poped list:',l2)
o=Linked()
o.Insertion(0,5)
o.Deletion(5)
        