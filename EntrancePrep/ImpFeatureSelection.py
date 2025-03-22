# def featureSelection(arr, k):
#     n = len(arr)
#     lst = []
#     res = []
#     for i in range(n-1):
#         if arr[i]> arr[i+1]:
#             lst.append(arr[i])
#     for j in range(k):
#         res.append(lst[j])
#     return res
# scores = [0.5, 0.2, 0.8, 0.1]
# print(featureSelection(scores, 2))

def featureSelection(arr, k):
    index_selection = [(ele, ind) for ind, ele in enumerate(arr)]
    index_selection.sort(reverse=True)
    return [ind for _, ind in index_selection[:k]]
print(featureSelection([0.5, 0.2, 0.8, 0.1], 2))