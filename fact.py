from math import factorial as fact
class factorial:
    def fact(self,n):
        if n==0:
            return 1
        else:
            print( n*fact(n-1))
o=factorial()
o.fact(5)