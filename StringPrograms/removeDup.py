def ordered(str):
    res = ''.join(set(str))
    print(f'The ordered string after removing duplicates: {res}')
def unordered(str):
    res = ''
    for i in str:
        if i in res:
            pass
        else:
            res += i
    print(f"The unordered result is: {res}")
string = 'inejiwaaa'
print(f'The original string is: {string}')
ordered(string)
unordered(string)

