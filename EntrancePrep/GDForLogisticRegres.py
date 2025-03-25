# import numpy as np
# def sigmoid(z):
#     return float(1/(1+np.exp(-z)))

# def GDLogistics(X, y, learning_rate=0.01, W=0, b=0):
#     Z = [W*x+b for x in X]
#     y_pred = [sigmoid(z) for z in Z]
#     error = [true - pred for (true, pred) in zip(y,y_pred)]
#     W_grad = (1/len(X)) * sum(err * x for (err,x) in zip(error, X))
#     b_grad = (1/len(X)) * sum(error)
#     W += learning_rate*W_grad
#     b += learning_rate*b_grad
#     return [W,b]

# X = [1, 2, 3]
# y = [0, 1, 1]

# print(GDLogistics(X,y))

import numpy as np
def sigmoid(z):
    return float(1/(1+np.exp(-z)))

def LogGD(X, y, learning_rate = 0.01, batch_size=2, epochs=50, W=0, b=0):
    n = len(X)
    for _ in range(epochs):
        for i in range(n):
            x_batch = X[i:i+batch_size]
            y_batch = y[i:i+batch_size]
            y_pred = [sigmoid(W*x+b) for x in x_batch]
            error = [true - pred for (true, pred) in zip(y_batch, y_pred)]
            W_grad = (1/len(x_batch)) * sum(err * x for (err, x) in zip(error, x_batch))
            b_grad = (1/len(x_batch)) * sum(error)
            W += learning_rate * W_grad
            b += learning_rate * b_grad
    return [W, b]
X = [1, 2, 3]
y = [0, 1, 1]

print(LogGD(X,y))
