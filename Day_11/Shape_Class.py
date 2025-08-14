import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area() method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

shapes = [Circle(5), Square(4), Triangle(3, 6)]

for s in shapes:
    print(f"{s.__class__.__name__} area: {s.area():.2f}")
