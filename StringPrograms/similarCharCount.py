# def count(str1, str2):
#     return len(set(str1.lower()).intersection(set(str2.lower())))
string1 = 'inezwa'
string2 = 'jihyaa'
# res = count(string1, string2)
# print(res)

# def count(str1, str2):
#     char_count = {}
#     for char in str1:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
    
#     counter = 0
#     for char in str2:
#         if char in char_count and char_count[char] > 0:
#             counter += 1
#             char_count[char] -= 1
#     return str(counter)
# result = count(string1, string2)
# print(result)

def count(str1, str2):
    char_count = {}
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    counter = 0
    for char in str2:
        if char in char_count and char_count[char] > 0:
            counter += 1
            char_count[char] -= 1
    return counter
res = count(string1, string2)
print(res)