class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Woof! My name is", self.name)
    
    def __str__(self):
        return f"Dog named {self.name}"