#Write a Python program to Check whether the given string is Palindrome using Stack 
l=[]
class Stack:
    def Push(self,a):
        l.append(a)
        a=l[::-1]
        if l==a:
            print(l,'it is a palindrome')
        else:
             print(l,'is not a palindrome')
o=Stack()
o.Push('M')
o.Push('0')
o.Push('M')
