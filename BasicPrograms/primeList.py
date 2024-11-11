# def prime(x,y):
#     lst = []
#     for i in range(x,y):
#         if i == 0 or i == 1:
#             continue
#         else:
#             for j in range(2, int(i**0.5)+1):
#                 if i % j ==0:
#                     break
#             else:
#                 lst.append(i)
#     return lst

# start = int(input("Enter the starting point for prime number list: "))
# end = int(input("Enter the end point of the range of list: "))
# num = prime(start, end)
# if len(num) == 0:
#     print("There are no prime numbers in this range.")
# else:
#     print("The list of prime numbers is", num)

# # def prime(x,y):
# #     lst = []
# #     for i in range(x,y):
# #         if i == 0 or i == 1:
# #             continue
# #         else:
# #             for j in range(2,int(i//2)+1):
# #                 if i % j == 0:
# #                     break
# #             else:
# #                 lst.append(i)
# #     return lst
# # start = int(input('Enter starting number: '))
# # end = int(input("enter ending point: "))
# # print(prime(start, end))

def prime(x , y):
    lst = []
    flag = 0
    for i in range(x,y):
        for j in range(2, i):
            if i % j == 0:
                flag = 1
                break
            else:
                flag = 0
        if flag == 0:
            lst.append(i)
    return lst
print(prime(2,20))
