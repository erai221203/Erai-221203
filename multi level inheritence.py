'''Multi level inheritence:
    the single inheritence in which 3 or more classes can be accessed'''
class si:
    def add(self):
        print('Hi from KCT')
class s(si):
    def sub(self):
        print('Bye')
class sii(s):
    def ub(self):
        print('Hello')
o=sii()
o.ub()