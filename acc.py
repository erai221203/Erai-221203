class Teacher:
    def name(self,Name):
        print('Public:',Name)
    def _age_(self,age):
        print('protected:',age)
    def __salary_(self,salary):
        print(salary)
o=Teacher()
o.name('Erai')
o._age_(20)
o._Teacher__salary_(20000)       

