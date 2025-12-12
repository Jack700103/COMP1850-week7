class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def __str__(self):
        return f"Person: {self.name}, {self.age} years old"