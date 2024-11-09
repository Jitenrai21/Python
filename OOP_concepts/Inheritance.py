class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def showAnimal(self):
        print(f"This is a {self.color} {self.name}.")

class Species(Animal):
    def __init__(self, name, color, species):
        super().__init__(name, color)
        self.species = species
    
    def showMammal(self):
        print(f"This is a {self.color} {self.name} of {self.species} species.")

class Dog(Species):
    def __init__(self, name, color, species, owner):
        super().__init__(name, color, species)
        self.owner = owner

    def showDog(self):
        print(f"This is a {self.color} {self.name} of {self.species} species and belongs to {self.owner}.")

a1 = Animal('Dog', 'Black')
# a1.showAnimal()

s1 = Species('Dog', 'Black', 'Mammal')
# s1.showMammal()

d1 = Dog('Dog', "Black", 'Mammal', 'Inez')
d1.showDog()