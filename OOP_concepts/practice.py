# #encapsulation
# class rectangle:
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth
    
#     def area(self):
#         area = self.length * self.breadth
#         print(f"Area : {area}")
    
#     def perimeter(self):
#         peri = 2*(self.length + self.breadth)
#         print(f"Perimeter : {peri}")

# r1 = rectangle(5,5)
# r1.area()
# r1.perimeter()

# #inhertence
# class animal:
#     def __init__(self, animal):
#         self.animal = animal
    
#     def showAnimal(self):
#         print(f'This is a {self.animal}')

# class dog(animal):
#     def __init__(self, animal, color):
#         super().__init__(animal)
#         self.color = color
    
#     def showDog(self):
#         print(f"This is a {self.color} {self.animal}.")

# d1 = dog('Dog', 'Black')
# d1.showAnimal()
# d1.showDog()

# #polymorphism
# class Nepal:
#     def name(self):
#         print('This is Nepal.')
#     def lang(self):
#         print('Nepalese is the native language.')
#     def cond(self):
#         print('It is a developing country.')
# class USA:
#     def name(self):
#         print('This is USA.')
#     def lang(self):
#         print('English is the native language.')
#     def cond(self):
#         print('It is a developed country.')

# n1 = Nepal()
# u1 = USA()

# for obj in (n1, u1):
#     obj.name()
#     obj.lang()
#     obj.cond()

# #polymorph by function

# class dog:
#     def sound(self):
#         return 'bark'

# class cat:
#     def sound(self):
#         return 'meow'

# def makeSound(animal):
#     return animal.sound()

# animals = [dog(), cat()]

# for animal in animals:
#     print(makeSound(animal))


# #private and protected variables
# class Person:
#     def __init__(self, name, age):
#         self._name = name
#         self.__age = age
    
#     def showAccess(self):
#         print(f"I am function inside the class, I can acces both private and protected variable.\nName:{self._name}\nAge:{self.__age}")

# class example(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#     def showAccess(self):
#         print(f'I only have acces to protected var. Name:{self._name}')

# p1 = Person('Inez', '22')
# p1.showAccess()

# e1 = example('Inez', '22')
# e1.showAccess()

# #abstraction
# from abc import ABC, abstractmethod
# class Animal(ABC):
#     def __init__(self, species, color, breed):
#         self.species = species
#         self.color = color
#         self.breed = breed
#     @abstractmethod
#     def showDetails(self):
#         pass

# class Dog(Animal):
#     def showDetails(self):
#         print(f'Species:{self.species}\nColor:{self.color}\nBreed:{self.breed}')

# d1 = Dog('Dog','Black', 'German')
# d1.showDetails()

# Encapsulation
class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        area = self.length * self.breadth
        print(f"Area:{area}")
    def perimeter(self):
        peri = 2 * (self.length + self.breadth)
        print(f"Perimeter:{peri}")
r1 = rectangle(5,5)
r1.area()
r1.perimeter()

# Inheritance
class animal:
    def __init__(self, species):
        self.species = species
    def showDetails(self):
        print(f"I am an specific {self.species}.")
class human(animal):
    def __init__(self, species, name):
        super().__init__(species)
        self.name = name
    def showHuman(self):
        print(f"I am specific {self.species} and called as {self.name}.")
h1 = human('Homo Sapiens','Human')
h1.showHuman()

#Protected and private
class person:
    def __init__(self, name, age):
        self._name = name
        self.__age = age
    def showdetails(self):
        print(f"Access to both {self._name} and {self.__age}.")
class person2(person):
    def __init__(self, name, age):
        super().__init__(name, age)
    def showName(self):
        print(f"Only access to Name:{self._name}")
p1 = person("Inez", '22')
p1.showdetails()
p2 = person2('Inez', '22')
p2.showName()

#Polymorphism
class Nepal:
    def country(self):
        print(f"This is Nepal.")
    def lang(self):
        print("The native langauge is Nepali.")
class USA:
    def country(self):
        print("This is USA.")
    def lang(self):
        print("English is the native language.")
n1 = Nepal()
u1 = USA()
for obj in (n1, u1):
    obj.country()
    obj.lang()

class dog:
    def sound(self):
        return 'bark'
class cat:
    def sound(self):
        return 'meow'
def makeSound(animal):
    return animal.sound()
animals = [dog(), cat()]
for animal in animals:
    print(makeSound(animal))

#abstraction
from abc import ABC, abstractmethod
class vehicle(ABC):
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color
    @abstractmethod
    def showDetails(self):
        pass
class car(vehicle):
    def __init__(self, name, model, color):
        super().__init__(name, model, color)
    def showDetails(self):
        print(f"This is a {self.color} {self.name} from {self.model} year.")
c1 = car('Asta', '2022', 'silver')
c1.showDetails()

