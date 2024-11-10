# num = int(input("Enter a number:"))
# factorial = 1
# for n in range(1, num+1):
#     factorial *= n
# print(f"Factorial for {num} is {factorial}.")

#by recursion and single line ternary operator
def facto(n):
    return 1 if (n==1 or n==0) else n * facto(n-1)
num = int(input("Enter number:"))
print(facto(num))