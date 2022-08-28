import math

""" The MyMath class, consisting of at least the following methods (you can add other methods as a bonus):
                          calculation of the circumference,
                          calculating the area of a circle,
                          calculating the volume of a cube,
                          calculation of the surface area of a sphere. """


class MyMath():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def volume(self):
        return 3 / 4 * 3.14 * self.radius ** 3

    def sphere_area(self):
        return 4 * math.pi * self.radius ** 2


r = int(input("Enter the radius of the circle: "))
obj = MyMath(r)
print("Area of a circle:", round(obj.area(), 2))
print("Circumference:", round(obj.perimeter(), 2))
print("Cube volume:", round(obj.volume(), 3))
print("Calculating the surface area of a sphere:", round(obj.sphere_area(), 2))
