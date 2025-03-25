# # method overriding
# class nepal:
#     def country(self):
#         print('This is Nepal.')
#     def lang(self):
#         print('Nepalese language is the national language.')
#     def cond(self):
#         print('It is a developing country.')

# class USA:
#     def country(self):
#         print('This is USA.')
#     def lang(self):
#         print("English is the native language.")
#     def cond(self):
#         print('USA is a developed country.')

# n1 = nepal()
# u1 = USA()

# for obj in (n1, u1):
#     obj.country()
#     obj.lang()
#     obj.cond()



#polymorphism by function
# class dog:
#     def sound(self):
#         return 'Dog is barking.'

# class cat:
#     def sound(self):
#         return 'Cat is meowing.'

# def makeSound(animal):
#     return animal.sound()

# animals = [dog(), cat()]

# for animal in animals:
#     print(makeSound(animal))

class USA:
    def name(self):
        print('This is USA.')
    def lang(self):
        print('The native tongue is English.')
class Nepal:
    def name(self):
        print('This is Nepal.')
    def lang(self):
        print('The native tongue is Nepali.')

objs = [USA(), Nepal()]  
for obj in objs:
    obj.name()
    obj.lang() 

class Dog:
    def sound(self):
        print('Bark!!')
class Cat:
    def sound(self):
        print('Meow!!')
def makeSound(animal):
    animal.sound()

animals = [Dog(), Cat()]

for animal in animals:
    makeSound(animal)