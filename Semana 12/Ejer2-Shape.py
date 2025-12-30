from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        self.area = self.calculate_area()
        self.perimeter = self.calculate_perimeter()

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass
    


class Circle(Shape):
    def __init__(self,radius):
        if radius <=0:
            raise ValueError("Radius must be a positive value.")
        self.radius = radius
        super().__init__()

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius
    
    def calculate_area(self):
        return (self.radius * self.radius) * 3.14


class Rectangle(Shape):
    def __init__(self, l, w):
        if l <=0 or w <=0:
            raise ValueError("Length and Width must be positive values.")
        self.l = l
        self.w = w
        super().__init__()

    def calculate_area(self):
        return self.l * self.w
    

    def calculate_perimeter(self):
        return 2*(self.l + self.w)


class Square(Shape):
    def __init__(self,side):
        if side <= 0:
            raise ValueError("Side must be a positice number.")
        self.side = side
        super().__init__()
    

    def calculate_area(self):
        return self.side * self.side
    
    def calculate_perimeter(self):
        return 4 * self.side


my_circle = Circle(12)
print(f"Circle perimeter: {my_circle.perimeter}")
print(f"Circle area: {my_circle.area}")

my_rectangle = Rectangle(4,6)
print(f"Rectangle perimeter: {my_rectangle.perimeter}")
print(f"Rectangle area: {my_rectangle.area}")

"""my_rectangle2 = Rectangle(-4,6)
print(f"Rectangle perimeter: {my_rectangle2.perimeter}")
print(f"Rectangle area: {my_rectangle2.area}")"""  # This should raise a ValueError


my_square = Square(5)
print(f"Square perimeter: {my_square.perimeter}")
print(f"Square area: {my_square.area}")