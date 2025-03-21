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

import numpy as np

X = np.array([1, 2, 3, 4, 5])
Y = np.array([2.1, 3.9, 6.0, 7.8, 9.9])

epochs = 50
learning_rate =0.1
W = 0
b = 0

for _ in range(epochs):
    y_pred = W*X + b
    error = y = y_pred
    W_grad = (2/len(X))* np.sum(error*W)
    b_grad = (2/len(X))* np.sum(error)
    W -= learning_rate*W_grad
    b -= learning_rate*b_grad

print(f'The weight and bais: {W:.2f} and {b:.2f}')

