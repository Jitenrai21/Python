# import string
# def check(str):
#     for char in str:
#         if char in string.punctuation:
#             print(f'The given string {str} cannot be accepted because of special characters.')
#             return
#     print(f"The given string {str} is accpeted.")
# check('Inezzz')
# check('Inezzwaaa###')

# #removing ith character
# def result(str, i):
#     str = str[:i] + str[i+1:]
#     return str
# string = 'Inezwaaa'
# i = 5
# res = result(string,i)
# print(res)

# #split and join
# def split(str):
#     list_str = str.split()
#     return list_str
# def join(list_str):
#     str = "-".join(list_str)
#     print(str)
# if __name__ == "__main__":
#     out = split("inez and jihyaa")
#     print(out)
#     join(out)

# #is binary or not
# def checkBinary(str):
#     b = '01'
#     count = 0
#     for char in str:
#         if char not in b:
#             count = 1
#             break
#     if count:
#         print("The given string is not binary.")
#     else:
#         print("The given string is binary.")
# checkBinary('01010101J')

# #uncommon words in string
# def uncommon(str1, str2):
#     count = {}
#     for word in str1.split():
#         count[word] = count.get(word, 0) + 1
#     for word in str2.split():
#         count[word] = count.get(word, 0) + 1
#     return [word for word in count if count[word] == 1]
# output = uncommon('Lets go party', 'Lets have party')
# print(output)

code = "'hello ' + 'world'"
output1 = eval(code)
print(output1)

code2 = "['a', 'b' ,'c'][0]"
res = eval(code2)
print(res)