class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type.")
    def __str__(self):
        return f"({self.x}, {self.y})"
point1 = Point(2, 3)
point2 = Point(4, 5)
result = point1 + point2
print("Point 1:", point1)        # (2, 3)
print("Point 2:", point2)        # (4, 5)
print("Result of Addition:", result)   # (6, 8)