def binarySearch(arr, target):
    first, last = 0, len(arr)-1
    res = -1
    # arr.sort()
    while first<=last:
        mid = (first+last)//2
        if arr[mid] == target:
            res = mid
            last = mid - 1
        elif arr[mid]<target:
            first = mid + 1
        else:
            last = mid - 1 
    return res
arr = [1,2,2,3,2,4,5]
target = 3
out = binarySearch(arr, target)
print(f'The looked for element is in {out+1}th position from left.')


