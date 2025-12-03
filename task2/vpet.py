class VirtualPet:
    def __init__(self, name, tiredness=0, fullness=10):
        self.name = name
        self.tiredness = tiredness  
        self.fullness = fullness    
    
    def play(self):
        if self.tiredness >= 8:  
            return f"{self.name} is too tired to play!"
        self.tiredness += 2
        self.fullness -= 2 
        return f"{self.name} played and is now less tired!"
    
    def feed(self):
        if self.fullness >= 15:  
            self.fullness = 15  
            return f"{self.name} is overfed!"
        self.fullness += 5
        return f"{self.name} ate and is now more full!"
    
    def sleep(self):
        self.tiredness = max(0, self.tiredness - 10) 
        return f"{self.name} slept and is now refreshed!"
    
    def __str__(self):
        return f"{self.name}: Tiredness={self.tiredness}, Fullness={self.fullness}"
    
    def __eq__(self, other):
        return (isinstance(other, VirtualPet) and
                self.name == other.name and
                self.tiredness == other.tiredness and
                self.fullness == other.fullness)
