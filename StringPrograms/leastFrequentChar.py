# def count(str):
#     all_freqs = {}
#     for char in str:
#         if char in all_freqs:
#             all_freqs[char] += 1
#         else:
#             all_freqs[char] = 1
#     res = min(all_freqs, key=all_freqs.get)
#     return res
string = 'Inneezz'
# print(count(string.lower()))

from collections import Counter
def count(str):
    counter = Counter(str)
    res = min(counter, key=counter.get)
    return res
print(count(string.lower()))