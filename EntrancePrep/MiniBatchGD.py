# def miniBatchGD(X, y, batch_size, learning_rate, W = 0, b = 0):
#     n = len(X)
#     for i in range(0, n, batch_size):
#         batch_X = X[i:i+batch_size]
#         batch_y = y[i:i+batch_size]
#         y_pred = [W*x + b for x in batch_X]
#         error = [true - pred for true, pred in zip(batch_y, y_pred)]
#         W_grad = (2/len(batch_X))*sum(err * x for err, x in zip(error, batch_X))
#         b_grad = (2/len(batch_y))* sum(error)
#         W += learning_rate*W_grad
#         b += learning_rate*b_grad
#     return W, b
# X, y = [1, 2, 3, 4], [2, 4, 6, 8]
# W, b = miniBatchGD(X, y, 2, 0.01)
# print(f'Weight:{W:.3f}, Bias:{b:.3f}')

import numpy as np

def MiniBatchGD(X, y, batch_size, learning_rate=0.01, epochs=50, W=0, b=0):
    n = len(X)
    for _ in range(epochs):
        for i in range(0,n,batch_size):
            x_batch = X[i:i+batch_size]
            y_batch = y[i:i+batch_size]
            y_pred = [W*x+b for x in x_batch]
            error = [true - pred for (true, pred ) in zip(y_batch, y_pred)]
            W_grad = (2/n) * sum(err * x for (err,x) in zip(error, x_batch))
            b_grad = (2/n) * sum(error)
            W += learning_rate*W_grad
            b += learning_rate*b_grad
    return W, b
X, y = [1, 2, 3, 4], [2, 4, 6, 8]
W, b = MiniBatchGD(X, y, 2)
print(f'Weight:{W:.2f}, bias:{b:.2f}')



