lst = [1,2,3,4,5]
# lst.reverse()
# print(lst)

# rev = list(reversed(lst))
# print(rev)

# rev = []
# for val in lst:
#     rev.insert(0, val)
# print(rev)

# rev = lst[::-1]
# print(rev)

rev = [lst[i] for i in range(len(lst)-1, -1, -1)] #len(a) - 1 is the starting index (the last index of a), -1 is the stopping point (the range stops before reaching -1, so it includes index 0), -1 is the step, which means the loop will decrement, moving backward through the list
print(rev)
