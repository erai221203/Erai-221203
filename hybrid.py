#Hybrid inheritence:
class get:
    def getin(self):
        self.a=int(input('Enter a:'))
        self.b=int(input('Enter b:'))
class Add(get):
    def add(self):
        self.getin()
        c=self.a+self.b
        print(c)
class Sub(get):
    def sub(self):
        self.getin()
        c=self.a-self.b
        print(c)
class Arith(Add,Sub):
    def arith(self):
        self.add()
        self.sub()
o=Arith()
o.arith()
