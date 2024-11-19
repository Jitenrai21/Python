#removing ith item
string = "hello world"
# rev = string.replace('o', '')
# print(rev)

# rev = ''
# for i in string:
#     if i != 'o':
#         rev += i
# print(rev)

rev = ''.join([c for c in string if c != 'o'])
print(rev)