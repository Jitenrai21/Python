lst1 = ['a','b','d','f','g','c','e']
lst2 = [0,0,1,1,2,0,1]
# lst = list(set(lst2)) #[0, 1, 2]
# lst.sort()
# res = []
# for i in lst:
#     for j in range(len(lst2)):
#         if lst2[j] == i:
#             res.append(lst1[j])
# print(res)

def sorting(lst1, lst2):
    pro = list(set(lst2))
    pro.sort()
    res = []
    for i in pro:
        for j in range(len(lst2)):
            if lst2[j] == i:
                res.append(lst1[j])
    return res
if __name__ == '__main__':
    output = sorting(lst1, lst2)
    print(f'The original list:{lst1}\nThe sorted list:{output}')

