import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def length(self):
        return math.sqrt((self.point2.x - self.point1.x)**2 + (self.point2.y - self.point1.y)**2)

class Triangle:
    def __init__(self, line1, line2, line3):
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3

    def perimeter(self):
        return self.line1.length() + self.line2.length() + self.line3.length()

# створення точок
point1 = Point(0, 0)
point2 = Point(3, 4)
point3 = Point(6, 0)

# створення відрізків за допомогою точок
line1 = Line(point1, point2)
line2 = Line(point2, point3)
line3 = Line(point3, point1)

# створення трикутника за допомогою відрізків
triangle = Triangle(line1, line2, line3)

# розрахунок та виведення периметру трикутника
print("Периметр трикутника:", triangle.perimeter())
