
#fibonacci series
# num = int(input("Enter a number for the series length: "))
# def fibo(n):
#     lst = [0,1]
#     if n<=0:
#         print("Incorrect input! Try positive number.")
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0,1]
#     for i in range(2,n):
#         lst.append(lst[-1] + lst[-2])
#     return lst
# print(fibo(num))

#nth fibionacci number
def fibo(n):
    if n<=0:
        print("Enter positive number!")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
print(fibo(10))