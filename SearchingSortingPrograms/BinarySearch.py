# #using recurssive
# def search(arr, high, low, x):
#     mid = (high + low) //2
#     if arr[mid] == x:
#         return mid
#     elif arr[mid] > x:
#         return search(arr, mid - 1, low, x)
#     elif arr[mid] < x:
#         return search(arr, low, mid + 1, x)
    
arr = [10, 21, 23, 34, 17]
# output = search(arr, len(arr)-1, 0, 23)
# print(f'The searched element lies at index {output}.')

#using iterative
def Search(arr, x):
    high = len(arr) -1
    low = 0
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            return mid
    return -1
res = Search(arr, 42)
if res!=-1:
    print(f'The looked for element is at index {res}.')
else:
    print('The looked output is not in the given list.')
       
    