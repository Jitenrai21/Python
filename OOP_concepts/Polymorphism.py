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

