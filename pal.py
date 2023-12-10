class palindrome:
    def reverse(self,a):
        a=input('Enter any word:')
        b=a[::-1]
        if a==b:
            print(a,'is a palindrome')
        else:
            print(a,'is not a palindrome')
o=palindrome()
o.reverse(0)
