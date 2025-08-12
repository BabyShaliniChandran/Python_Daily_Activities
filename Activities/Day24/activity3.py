class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"Circle: {(3.14 * self.radius ** 2)}"

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return f"Rectangle:{self.width * self.height}"

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return f"Triangle:{0.5 * self.base * self.height}"

circle=Circle(2)
rectangle=Rectangle(3,4)
triangle=Triangle(3,5)

for shape in [circle,triangle,rectangle]:
    print(f'Area of {shape.area()}')
