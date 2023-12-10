class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        a=self.length * self.width
        print(a)
    def perimeter(self):
        p=2 * (self.length + self.width)
        print(p)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print(3.14 * self.radius * self.radius)
    def perimeter(self):
        print(2 * 3.14 * self.radius)
rectangle = Rectangle(5, 3)
circle = Circle(4)
print("Rectangle")
rectangle.area()
rectangle.perimeter()
print("\nCircle")
circle.area()
circle.perimeter()