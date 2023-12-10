class ram:
    def pro(self):
        print('Hi from class ram')
class sam(ram):
    def pro(self):
        super().pro()
        print('Hi from class sam')
class kiran(sam):
    def pro(self):
        super().pro()
        print('Hi from class kiran')

kiran().pro()
ram().pro()