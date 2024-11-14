def evenOdd(start, end):
    even = []
    odd = []
    for i in range(start, end+1):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd

starting = int(input("Enter the start for the range: "))
ending = int(input("Enter the end of the range: "))

even, odd = evenOdd(starting, ending)
print(f"The list of even and odd numbers within the range of {starting} and {ending} are\nEven:{even}\nOdd:{odd}")