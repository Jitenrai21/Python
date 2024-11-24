#extracting unique values from dictionary
dic = {'a':[1,3,2], 'b':[3,4,5], 
       'c': [7,6,8,5]}
lst = list(sorted({ele for val in dic.values() for ele in val }))
print(lst)

pre = []
res = []
for i in dic.values():
    pre.extend(i)
for j in pre:
    if j not in res:
        res.append(j)
res.sort()
print(res)

#sum of value in dict
# def sum(dic1):
#     sum = 0
#     for i in dic1.values(): #for i in dic:
#         sum = sum + i # sum = sum + dic[i]
#     return sum
# dic1 = {'a':100, 'b':200, 'c':300}
# print(sum(dic1))

def returnSum(dic):
    lst = []
    resLst = []
    for i in dic.values():
        lst.extend(i)
    for j in lst:
        if j not in resLst:
            resLst.append(j)
    add = sum(resLst)
    return add
print(returnSum(dic))