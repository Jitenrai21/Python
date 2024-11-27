
def check(arr, target):
    for idx in range(len(arr)):
        if arr[idx] == target:
            return idx

    return -1
if __name__ == '__main__':
    arr = [11, 22, 34, 23, 45,55,66]
    target = 23
    out = check(arr, target)
    if out != -1:
        print('The searched element is at index',out)
    else:
        print("The looked for element doesn't exist.")