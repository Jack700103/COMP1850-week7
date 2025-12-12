import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius * self.radius
    
    def circumference(self):
        return 2 * math.pi * self.radius
    
    def __str__(self):
        return f"Circle with radius {self.radius}"
