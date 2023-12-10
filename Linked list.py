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
        