# def power(x,y):
#     if y == 0:
#         return 1
#     if y % 2 == 0:
#         return power(x, y//2) * power(x, y//2)
#     return x * power(x,y//2) * power(x,y//2)

# def order(x):
#     n = 0
#     while (x!=0):
#         n+=1
#         x=x//10
#     return n

# def isArmstrong(x):
#     n = order(x)
#     sum = 0
#     temp = x
#     while temp != 0:
#         r = temp % 10
#         sum += power(r,n)
#         temp = temp//10
#     if sum == x:
#         print(f"{x} is an armstrong number.")
#     else:
#         print(f'{x} isnot an armstrong number.')

# isArmstrong(153)

#Without the power function
n = int(input("Enter the number to check: "))
s = n
sum = 0
x = len(str(n))
while s != 0:
    r = s % 10
    sum = sum + (r**x)
    s = s // 10
if (sum == n):
    print(f'{n} is an armstrong number.')
else:
    print(f'{n} is not an armstrong number.')