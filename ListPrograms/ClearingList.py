lst = [1,2,3,4,5,6]
print(lst)

#built-in function
# lst.clear()
# print(lst)

#declaring list again
# lst = []
# print(lst)

#using del
# del lst[:]
# print(lst)

#using pop function
# while len(lst) != 0:
#     lst.pop()
# print(lst)

#by slicing
# lst = lst[:0]
# print(lst)

#by function
def clear_list(lst):
    lst = [item for item in lst if False]
    return lst
ans = clear_list(lst)
print(ans)
