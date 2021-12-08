import math

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        print((math.pi) * (self.r * self.r))

    def perimeter(self):
        print(2 * math.pi * self.r)

num=int(input())

obj = Circle(num)

obj.area()
obj.perimeter()