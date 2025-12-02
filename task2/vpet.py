# Define a class called VirtualPet with the following attributes:
# (1) name - the name of the pet
# (2) energy - the energy points for the pet, default value is 10
# (3) hunger - the pet's hunger level, default value is 0
# When an instance of VirtualPet is created, only the name is needed, as a minimum, for the __init__ method





# This class has the following methods:
# (1) play() - If energy<2, report in the format "{name} is too tired to play!".
#     Otherwise simulate playing by reducing the energy by 2 and increase the hunger by 2.
# (2) feed() - Simulate feeding the pet and reducing hunger by 3.
#     If hunger is less than 0, report in the format "{name} is overfed!" and reset hunger to 0.
# (3) sleep() - let the pet sleep and increase the energy by 10.
# (4) __str__() - returns the details of the pet in the format "{name} has {energy} energy points and hunger level {hunger}", 
#     e.g., "Timmy has 100 energy points and hunger level 0"
# (5) __eq__() - returns True if all attributes are identical, False otherwise

# You should test each method in your code before submission.
# Check that attributes are modified as expected
# For example:

''' Tests
Pet = VirtualPet("Timmy",4,3)
print(Pet)
Pet.play()
print(Pet)
Pet.feed()
print(Pet)
Pet.sleep()
print(Pet)
'''

# VirtualPet class simulating a digital pet with energy and hunger management
class VirtualPet:
    """A virtual pet that can play, eat, and sleep.
    
    Attributes:
        name (str): The name of the pet.
        energy (int): The energy points of the pet, default is 10.
        hunger (int): The hunger level of the pet, default is 0.
    """
    
    def __init__(self, name, energy=10, hunger=0):
        """Initialize a VirtualPet instance with specified attributes."""
        self.name = name
        self.energy = energy
        self.hunger = hunger

    def play(self):
        """Simulate playing activity. Reduces energy by 2 and increases hunger by 2.
        Prints a message if the pet is too tired to play.
        """
        if self.energy < 2:
            print(f"{self.name} is too tired to play!")
        else:
            self.energy -= 2
            self.hunger += 2

    def feed(self):
        """Simulate feeding the pet. Decreases hunger by 3.
        Prints a message if overfeeding occurs and resets hunger to 0.
        """
        self.hunger -= 3
        if self.hunger < 0:
            print(f"{self.name} is overfed!")
            self.hunger = 0

    def sleep(self):
        """Simulate sleeping activity. Increases energy by 10."""
        self.energy += 10

    def __str__(self):
        """Return formatted string representation of the pet's state."""
        return f"{self.name} has {self.energy} energy points and hunger level {self.hunger}"

    def __eq__(self, other):
        """Check equality between two VirtualPet instances based on all attributes."""
        return (isinstance(other, VirtualPet) and
                self.name == other.name and
                self.energy == other.energy and
                self.hunger == other.hunger)