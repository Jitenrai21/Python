lst = [(1,2),(1,3),(2,3),(2,4),(3,4,5),(3,7)]
res = []
for sub in lst:
    if res and res[-1][0] == sub[0]:
        res[-1].extend(sub[1:])
    else:
        res.append([ele for ele in sub]) #[[1, 2, 3], [2, 3, 4], [3, 4, 5, 7]]
res = list(map(tuple, res))
print(res)
