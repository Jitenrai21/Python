# elements interchanged
lst = [21,31,41,51,61]
lst[1], lst[2] = lst[2], lst[1]
print(lst)

# count = 0
# for val in lst:
#     count +=1
# print(f"Length of the given list is: {count}")

# #searching elements in list
# lst1 = [21,31,41,51,61]
# key = int(input("Enter the desired number to searched: "))
# flag = False
# i = 1
# for val in lst1:
#     if val != key:
#         i += 1
#     elif val == key:
#         flag = True
#         break
# if flag:
#     print(f"The looked for element is in the list located at {i}th position.")
# else:
#     print("The looked for element is not in the list.")

# #Smallest in the list
# smallest = lst[0]
# for val in lst:
#     if val < smallest:
#         smallest = val
# print(f"Smallest element is {smallest}.")

#by sorting
# lst.sort()
# smallest = lst[0]
# print(smallest)

#second greatest number
num = sorted(lst)[-2]
print(num)

#n number of greatest numbers
def NGrestesNumbers(lst, n):
    rev = []
    for i in range(n):
        max = 0
        for j in range(len(lst)):
            if lst[j] > max:
                max = lst[j]
        lst.remove(max)
        rev.append(max)
    print(rev)
NGrestesNumbers(lst, 2)

#cloning list by slicing
cloneList = lst[:]

#by extend function
# cloneList = []
# cloneList.extend(lst)
print(f"This is the clone of original list: {cloneList}.")

#counting elements
demo = [1,2,3,4,1,2,3,1,2,3,4,5,6,5,6,6]
print(demo.count(6))

def count(lst):
    count = 0
    for val in lst:
        if val ==6:
            count += 1
    return count
print(count(demo))