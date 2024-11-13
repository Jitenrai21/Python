def rotate(arr, l, n):
    temp = []
    i = 0
    while i < n:
        temp.append(arr[i])
        i = i + 1
    i = 0
    while n < l:
        arr[i] = arr[n]
        i += 1
        n += 1
    arr[:] = arr[: i] + temp
    return arr
if __name__ == '__main__':
     arr1 = [1,2,3,4,5,6]
     n = int(input("Enter the desired number: "))
     output = rotate(arr1, len(arr1), n)
     print(output)