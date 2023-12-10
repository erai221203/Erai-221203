'''Multiple inheritence:
    The data in different classes can be accessed by external classes with multiple classes.'''
print('Multiple Inheritence')
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