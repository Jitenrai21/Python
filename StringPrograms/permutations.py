# from itertools import permutations

# str = 'INEZ'
# per = permutations(str)

# res = []
# for i in list(per):
#     if i not in res:
#         res.append(i)
#         print(''.join(i))

# def generate_permutation(string):
#     if len(string) == 1:
#         return [string]     
    
#     lst = []
#     for i in range(len(string)):
#         fixed = string[i]
#         remaining = string[:i] + string[i+1:]
#         for perm in generate_permutation(remaining):
#             lst.append(fixed + perm)
#     return lst
# string = 'INEZ'
# s = set(generate_permutation(string))
# print('The possible permutations are:', end='')
# for perm in s:
#     print(perm)
        
def generate_permutaion(string):
    if len(string) == 1:
        return [string]
    lst = []
    for i in range(len(string)):
        fixed = string[i]
        remaining = string[:i] + string[i+1:]
        for perm in generate_permutaion(remaining):
            lst.append(fixed + perm)
    return lst
z = set(generate_permutaion('JIHYA'))
for perm in z:
    print(perm)



