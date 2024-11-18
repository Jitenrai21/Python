def count(lst):
    repeated = []
    for i in range(len(lst)):
        k = i + 1
        for j in range(k, len(lst)):
            if lst[i] == lst[j] and lst[i] not in repeated:
                repeated.append(lst[i])
    return repeated
lst1 = [1,2,2,2,3,3,4,4,5,6,1,7,8]
print(count(lst1))

def repeat(lst):
    unique = []
    duplicate = []
    for i in lst:
        if i not in unique:
            unique.append(i)
        elif i not in duplicate:
            duplicate.append(i)
    return duplicate
print(repeat(lst1))

repeated = list(set([x for i,x in enumerate(lst1) if lst1.count(x) > 1]))
print(repeated)