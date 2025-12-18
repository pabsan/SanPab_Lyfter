class circle:
    def __init__(self, radius=None):
        self.radius = radius
    

    def get_area(self):
        if self.radius is None:
            print("Radius not defined")
            return None
        else:
            return 3.14 * (self.radius ** 2)

circle1 = circle(5)
print("Area of circle with radius 5:", circle1.get_area())

circle2 = circle()
print("Area of circle with undefined radius:", circle2.get_area())

circle1 = circle(10)
print("Area of circle with radius 10:", circle1.get_area())