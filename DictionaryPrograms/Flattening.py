from itertools import product
dic = {'Order':[1,2,3],'Months':['Jan', 'Feb', 'March']}
res = dict(zip(dic['Order'], dic['Months']))
print(res)

x = list(dic.values()) #[[1, 2, 3], ['Jan', 'Feb', 'March']]
a = x[0]
b = x[1]
d = {}
for i in range(len(a)):
    d[a[i]] = b[i]
print(str(d))
print(d)
