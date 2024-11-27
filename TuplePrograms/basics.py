#size of tuple
tuple1 = ('Inez', 22, 'Jihyaa', 24)
print('The size of the tuple is: '+str(tuple1.__sizeof__())+' bytes.')

#k max and min elements
tup1 = (2, 23, 45, 21, 53, 13)
res = []
tup1 = list(sorted(tup1))
k = 2
for idx, ele in enumerate(tup1):
    if idx < k or idx >= len(tup1)-k:
        res.append(ele)
res = tuple(res)
print(str(res))
#by slicing
l = 1
tup2 = tup1[:l] + tup1[len(tup1)-l:]
out = tuple(tup2)
print(out)

#adding list and tuple
tupl1 = (1,2,3,4)
lst1 = [4,5,6]
lst1 += tupl1
print(lst1)

sum = tupl1 + tuple(lst1)
print(sum)

#flattening
lstTup = ([1,2],[2,3,4],[1,2,3,4])
# res = tuple(sum(lstTup,[]))
res = []
for i in lstTup:
    res.extend(i)
res = tuple(res)
print(res)