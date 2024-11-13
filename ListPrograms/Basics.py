# elements interchanged
lst = [21,31,41,51,61]
lst[1], lst[2] = lst[2], lst[1]
print(lst)

count = 0
for val in lst:
    count +=1
print(f"Length of the given list is: {count}")

#searching elements in list
lst1 = [21,31,41,51,61]
key = int(input("Enter the desired number to searched: "))
flag = False
i = 1
for val in lst1:
    if val != key:
        i += 1
    elif val == key:
        flag = True
        break
if flag:
    print(f"The looked for element is in the list located at {i}th position.")
else:
    print("The looked for element is not in the list.")
