class Rectangle:
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
rectangle1 = Rectangle()                
rectangle2 = Rectangle(5)               
rectangle3 = Rectangle(3, 4)          
print("Rectangle 1 Area:", rectangle1.area())   
print("Rectangle 2 Area:", rectangle2.area())   
print("Rectangle 3 Area:", rectangle3.area())