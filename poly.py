class overloading:
    def product(a,b):
        result = a*b
        print(result)
    def product(a,b,c):
        result  = a* b*c
        print(result)
    def product(a ,b,c):
        result  = a* b* c
        print(result)
Load=overloading()
Load.product(20,10)
Load.product(2,3,2) 
#this will give output of 12
Load.product(2.2,3.4,2.3) 
# this will give output of 17.985999999999997
