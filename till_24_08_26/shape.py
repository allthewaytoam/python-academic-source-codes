import math

class shape:
    def __init__(self, r):
        self.radius = r

class circle(shape):
    def __init__(self, r):
        super().__init__(r)
    def calarea(self):
        return math.pi * math.pow(self.radius, 2)

class sphere(shape):
    def __init__(self, r):
        super().__init__(r)
    def calvolume(self):
        return (4/3) * math.pi * math.pow(self.radius, 3)

def main():
    r = float(input("Enter the radius: "))
    c = circle(r)
    s = sphere(r)
    print(f"Area of Circle: {c.calarea()}")
    print(f"Volume of Sphere: {s.calvolume()}")

if __name__ == "__main__":
    main()