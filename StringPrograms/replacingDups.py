# string_org = 'Inez is a very good girl. Inez is very hardworking, smart. Jihya is a good boy. Jihya takes good care of Inez.'
# repl_str = {'Inez':'She','Jihya':'He'}
# print(f"This is the original string:\n{string_org}")
# str_list = string_org.split(" ")
# res = set()
# for idx, ele in enumerate(str_list):
#     if ele in repl_str:
#         if ele in res:
#             str_list[idx] = repl_str[ele]
#         else:
#             res.add(ele)
# res = ' '.join(str_list)
# print(str(res))

org = 'Jihyaa is good but Jihyaa is arrogant. Inez is good and Inez is kind.'
repl = {'Jihyaa':'He', 'Inez':'She'}
res = set()
org_list = org.split(" ")
for idx, ele in enumerate(org_list):
    if ele in repl:
        if ele in res:
            org_list[idx] = repl[ele]
        else:
            res.add(ele)
output = ' '.join(org_list)
print(output)

org_str = 'Inez is the one to cure it. Inez is the lighthouse.'
place = ['Inez']
rep = 'Love'
out = ' '.join([rep if idx in place else idx for idx in org_str.split()])
print(out)

