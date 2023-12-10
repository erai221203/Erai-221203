class string:
    def _init_(self):
        self.l1=[]
        self.l2=[]
    def append(self,str):
        for char in str:
            self.l1.append(char)
        print(self.l1)
    def pop(self):
        while self.l1:
            c=self.l1.pop()
            self.l2.append(c)
        print(self.l2)
        if self.l1==self.l2:
            print("yes")
        else:
            print("no")
o=string()
o.append("mam")
o.pop()