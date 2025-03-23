# import numpy as np

# X = np.array([1, 2, 3, 4, 5])
# Y = np.array([2.1, 3.9, 6.0, 7.8, 9.9])

# epochs = 50
# learning_rate =0.1
# W = 0
# b = 0

# for _ in range(epochs):
#     y_pred = W*X + b
#     error = y_pred - Y
#     W_grad = (2/len(X))* np.sum(error*W)
#     b_grad = (2/len(X))* np.sum(error)
#     W -= learning_rate*W_grad
#     b -= learning_rate*b_grad

# print(f'The weight and bais: {W:.2f} and {b:.2f}')

import numpy as np

X = np.array([1,2,3,4,5])
y = np.array([2, 4, 6, 8, 10])
# X, y = [1, 2, 3, 4], [2, 4, 6, 8]

learning_rate = 0.01
epochs = 50
W = 0
b= 0

for _ in range(epochs):
    y_pred = W * X + b
    error = y - y_pred
    W_grad = (2/len(X)) * np.sum(error*X)
    b_grad = (2/len(X)) * np.sum(error)
    W += learning_rate*W_grad
    b += learning_rate*b_grad

print(f'Weight:{W:.2f}, bais={b:.2f}')
