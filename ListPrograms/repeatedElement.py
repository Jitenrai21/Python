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