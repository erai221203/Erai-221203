'''Single Inheritence:
    The data in different classes can be accessed by external classes with only single class '''
class si:
    def add(self):
        print('Hi from KCT')
class s(si):
    def sub(self):
        print('Bye')
o=s()
o.add()
o.sub()