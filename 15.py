#Write a Python program to reverse a stack
l=[]
class Stack:
    def Push(self,a):
        l.append(a)
        a=l[::-1]
        print('reversed stack:',a)
o=Stack()
o.Push('M')
o.Push('0')
o.Push('M')
