# #extracting unique values from dictionary
# dic = {'a':[1,3,2], 'b':[3,4,5], 
#        'c': [7,6,8,5]}
# lst = list(sorted({ele for val in dic.values() for ele in val }))
# print(lst)

# pre = []
# res = []
# for i in dic.values():
#     pre.extend(i)
# for j in pre:
#     if j not in res:
#         res.append(j)
# res.sort()
# print(res)

# #sum of value in dict
# # def sum(dic1):
# #     sum = 0
# #     for i in dic1.values(): #for i in dic:
# #         sum = sum + i # sum = sum + dic[i]
# #     return sum
# # dic1 = {'a':100, 'b':200, 'c':300}
# # print(sum(dic1))

# def returnSum(dic):
#     lst = []
#     resLst = []
#     for i in dic.values():
#         lst.extend(i)
#     for j in lst:
#         if j not in resLst:
#             resLst.append(j)
#     add = sum(resLst)
#     return add
# print(returnSum(dic))

#removing item
dict1 = {'Inez':22,'Jihyaa':'24','Cairo':5}
print(dict1)
# del dict1['Cairo']
# print(dict1)
dict1.pop('Cairo')
print(dict1)

#sorting
from operator import itemgetter
lst = [{'Name':'Jihyaa', 'Age':24}, {'Name':'Inez', 'Age':22}]
print(lst)
res = sorted(lst, key=itemgetter('Age'))
print(res)

#merging two dictionaries
d1 = {'a':1, 'b':2}
d2 = {'d':4, 'c':3}
d1.update(d2)
print(d1)
# d3 = d1 | d2
d3 = {**d1, **d2}
print(d3)
def sorting(d1, d2):
    for i in d2.keys():
        d1[i] = d2[i]
    return d1
print(sorting(d1, d2))
