class VirtualPet:
    def __init__(self, name, energy=10, hunger=0):
        self.name = name
        self.energy = energy
        self.hunger = hunger

    def play(self):
        if self.energy < 2:
            print(f"{self.name} is too tired to play!")
        else:
            self.energy -= 2
            self.hunger += 2

    def feed(self):
        self.hunger -= 3
        if self.hunger < 0:
            print(f"{self.name} is overfed!")
            self.hunger = 0

    def sleep(self):
        self.energy += 10

    def __str__(self):
        return f"{self.name} has {self.energy} energy points and hunger level {self.hunger}"

    def __eq__(self, other):
        return (isinstance(other, VirtualPet) and
                self.name == other.name and
                self.energy == other.energy and
                self.hunger == other.hunger)
    

class Tamagotchi:
    def __init__(self):
        self.tiredness = 0
        self.fullness = 10
    
    def play(self):
        if self.tiredness >= 8:
            return "Timmy is too tired to play!"  
        self.tiredness += 2
        return "Timmy played and is now less tired!"
    
    def feed(self):
        if self.fullness >= 15: 
            return "Timmy is overfed!"  
        self.fullness += 5
        return "Timmy ate and is now more full!"