class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        Area = self.length * self.breadth
        print(f"Area: {Area}")
    
    def perimeter(self):
        perimeter = 2 * (self.length + self.breadth)
        print(f"Perimeter: {perimeter}")

    def __str__(self):
        return f"Length:{self.length} and Breadth:{self.breadth}"
    
R1 = rectangle(5,5)
print(R1)
R1.area()
R1.perimeter()