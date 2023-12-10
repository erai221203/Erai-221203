'''Single Inheritence:
    The data in different classes can be accessed by external classes with only single class '''
class si:
    def add(self):
        print('hi')
class s(si):
    def sub(self):
        print('bye')
o=s()
o.add()
o.sub()
'''Multiple inheritence:
    The data in different classes can be accessed by external classes with multiple classes.'''
class Add:
    def add(self):
        a=int(input('Enter a:'))
        b=int(input('Enter b:'))
        c=a+b
        print(c)
class Sub:
    def sub(self):
        a=int(input('Enter a:'))
        b=int(input('Enter b:'))
        c=a-b
        print(c)
class Math(Add,Sub):
    def base(self):
        self.add()
        self.sub()
o=Math()
o.base()
'''Multi level inheritence:
    the single inheritence in which 3 or more classes can be accessed'''
class si:
    def add(self):
        print('hi')
class s(si):
    def sub(self):
        print('bye')
class sii(s):
    def ub(self):
        print('hello')
o=sii()
o.add()
o.sub()
o.ub()
'''Hierarchial level inheritence:
    the Multi level inheritence iinheritence in which 1st class is given to access by all class.'''
class gett:
    def getin(self):
        self.a=int(input('Enter a:'))
        self.b=int(input('Enter b:'))
class Add(gett):
    def add(self):
        self.getin()
        c=self.a+self.b
        print(c)
class Sub(gett):
    def sub(self):
        self.getin()
        c=self.a-self.b
        print(c)
o=Add()
o.add()
o=Sub()
o.sub()
'''Hybrid inheritence:
    '''
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
