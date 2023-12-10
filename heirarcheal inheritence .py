'''Hierarchial level inheritence:
    the Multi level inheritence in which 1st class is given to access by all class.'''
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
Add().add()
Sub().sub()
