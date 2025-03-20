# Encapsulation
class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def Area(self):
        Area = self.length * self.breadth
        print(f'Area : {Area}')

    def Perimeter(self):
        Peri = 2 * (self.length + self.breadth)
        print(f'Perimeter : {Peri}')

r1 = rectangle(5,5)
r1.Area()
r1.Perimeter()

# Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    
    def showAnimal(self):
        print(f'This is a {self.name}.')

class Species(Animal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species
    
    def showSpecies(self):
        print(f'This {self.name} is of {self.species} species.')

A1 = Animal('Human')
S1 = Species('Human','Homo Sapiens')

A1.showAnimal()
S1.showAnimal()
S1.showSpecies()

# Protected and Private Variable Concept
class Man:
    def __init__(self, name, age):
        self._name = name
        self.__age = age
    
    def fullAccess(self):
        print(f'I have access to both {self._name} and {self.__age}.')
    
class Name(Man):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def partialAccess(self):
        print(f'Only access to {self._name} by inheritance.')

M1 = Man('Jiten', '25')
N1 = Name('Jiten', '25')  

M1.fullAccess()
N1.partialAccess()

# Polymorphism
# method overriding
class Nepal:
    def Name(self):
        print('This is Nepal.')
    def Lang(self):
        print('The native tongue is Nepali.')

class USA:
    def Name(self):
        print('This is USA.')
    def Lang(self):
        print('The native tongue is English.')

N1 = Nepal()
U1 = USA()

for obj in (N1, U1):
    obj.Name()
    obj.Lang()

# Method Overloading
class Dog:
    def sound(self):
        print('Bark!')

class Cat:
    def sound(self):
        print('Meow!')

def makeSound(animal):
    return animal.sound()

animals = [Dog(), Cat()]

for animal in animals:
    makeSound(animal)