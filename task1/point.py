class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def display(self):
        print("Point at:", self.x, self.y)

    def get_coordinates(self):
        return (self.x, self.y)

    def distance_to_origin(self):
        return (self.x**2 + self.y**2)**0.5
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
