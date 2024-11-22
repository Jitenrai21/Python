string_org = 'Inez is a very good girl. Inez is very hardworking, smart. Jihya is a good boy. Jihya takes good care of Inez.'
repl_str = {'Inez':'She','Jihya':'He'}
print(f"This is the original string:\n{string_org}")
str_list = string_org.split(" ")
res = set()
for idx, ele in enumerate(str_list):
    if ele in repl_str:
        if ele in res:
            str_list[idx] = repl_str[ele]
        else:
            res.add(ele)
res = ' '.join(str_list)
print(str(res))