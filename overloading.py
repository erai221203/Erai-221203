class overloading:
    def product(self,*args):
        sum=0
        for i in args:
            sum=sum+i
            print(sum)
        print(sum)
    def product(self,a=None,b=None,c=None,d=None):
        if a!=None and b!=None and c!=None and d!=None:
            print(a+b+c+d)
        elif a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None :
            print(a+b)   
        else:
               print(a)
   
Load=overloading()
#Load.product(20,10)
Load.product(2,3,4) 
