class cons:
    def __init__(self,name,age):
        self.n=name
        self.a=age
        print(self.n)
        print(age)
class c(cons):
    def __init__(self,name):
        print(self.name)
    
o=cons('adg',16)
o=c('af')

