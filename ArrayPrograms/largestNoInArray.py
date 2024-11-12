def larg(arr, n):
    max = arr[0]
    for i in range(n):
        if arr[i] > max:
            max = arr[i]
    return max
if __name__ == '__main__':
    arr = [12, 13, 199, 190,210, 100, 122]
    n = len(arr)
    ans = larg(arr,n)
    print(f"From the given array {arr}, {ans} is the greatest number.")
