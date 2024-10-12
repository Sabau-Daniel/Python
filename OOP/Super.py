

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    
    def describe(self):
        print(f"It is {self.color} and {"filled" if self.is_filled else "not filled"}")
    


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with a radius of {self.radius}cm^2")
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, height ):
        super().__init__(color, is_filled)
        self.height = height

class Triangle(Shape):
    def __init__(self, color, is_filled, height, weight):
        super().__init__(color, is_filled)
        self.height = height
        self.weight = weight


circle = Circle("red", True, 5)
square = Square("blue", False, 7)
triangle = Triangle("Orange", True, 4, 3)

circle.describe()
print(circle.color)
print(circle.is_filled)
print(circle.radius)
