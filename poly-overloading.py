
class overloading:
    def product(self,*args):
        sum=0
        for i in args:
            sum=sum+i
        print(sum)
    '''def product(self,a=None,b=None,c=None,d=None,e=None):
        if a!=None and b!=None and c!=None and d!=None and e!=None:
            print(a+b+c+d+e)
        elif a!=None and b!=None and c!=None and d!=None:
            print(a+b+c+d)
        elif a!=None and b!=None and c!=None:
            print(a+b+c)   
        elif a!=None and b!=None:
            print(a+b)
        else:
               print(a)
   '''
Load=overloading()
Load.product(int(list(input('Enter:'))))
