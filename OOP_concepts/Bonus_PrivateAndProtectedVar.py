class Person:
    def __init__(self, name, age):
        self._name = name #protected
        self.__age = age #private

    def showAccess(self):
        print("I can access both private and protected variable.")
        print(f'My name is {self._name} and I am {self.__age} years old.')

class Name(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def showAccess(self):
        print("Only access to protected variable by the rule of inheritence.")
        print(f"My name is {self._name}.")

p1 = Person('Inez', '22')
p1.showAccess()

n1 = Name('Inez', '22')
n1.showAccess()