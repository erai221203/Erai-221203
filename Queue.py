#Queue
print('******Queue******')
l1=[1,2,3,4,5]
class Queue:
    def Enqueue(self,a):
        l1.append(a)
        print(a,'is added to the list l:',l1)
    def Dequeue(self,a):
        l1.pop(0)
        print('Poped list:',l1)
o=Queue()
o.Enqueue(0)
o.Dequeue(0)
print('\t') 