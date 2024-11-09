from abc import ABC, abstractmethod

class car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    @abstractmethod
    def showDetails(self):
        pass

    def acc(self):
        print('Speed up...')

    def brake(self):
        print('Car stopped!')

class asta(car):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)
    
    def showDetails(self):
        print(f"Brand:{self.brand}\nModel:{self.model}\nYear:{self.year}")

    def acc(self):
        print('Speed up...')

    def brake(self):
        print('Car stopped!')

c1 = asta('Hyundai', 'Grand i10', '2022')
c1.showDetails()
c1.acc()
c1.brake()
