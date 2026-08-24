import math

class triangle:
    def __init__(self, a,b,c,d,e,f):
        self.side1 = a
        self.side2 = b
        self.side3 = c
        self.angle1 = d
        self.angle2 = e
        self.angle3 = f

class equilateral(triangle):
    def __init__(self, a):
        area = 60
        super().__init__(a,a,a,area,area,area)
    def calarea(self):
        return (math.sqrt(3)/4) * (self.side1 ** 2)
    def tan_angle(self):
        a1 = math.tan(self.angle1)
        a2 = math.tan(self.angle2)
        a3 = math.tan(self.angle3)
        return a1, a2, a3

class scalene(triangle):
    def __init__(self, a,b,c,d,e,f):
        super().__init__(a,b,c,d,e,f)

    def calPerimeter(self):
        return self.side1 + self.side2 + self.side3

    def calArea(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))


def main():
    e = equilateral(5)
    print(f"Area of Equilateral Triangle: {math.ceil(e.calarea())}")
    print(f"Tangent of angles: {e.tan_angle()}")
    s = scalene(3,4,5,60,60,60)
    print(f"Perimeter of Scalene Triangle: {s.calPerimeter()}")
    print(f"Area of Scalene Triangle: {math.ceil(s.calArea())}")

if __name__ == "__main__":
    main()
