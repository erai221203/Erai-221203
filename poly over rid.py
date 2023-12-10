class ram:
    def pro(self):
        print('asfa')
class sam(ram):
    def pro(self):
        super().pro()
        print('sdg')
class ki(sam):
    def pro(self):
        super().pro()
        print('asf')

o=ki()
o.pro()