lst = [1,2,3,4,5]
rev_ele = [2,3,4]
# for val in rev_ele:
#     if val in lst:
#         lst.remove(val)
# print(lst) 

lst = [item for item in lst if item not in rev_ele]
print(lst)
