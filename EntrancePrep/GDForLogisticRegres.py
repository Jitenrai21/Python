import numpy as np
def sigmoid(z):
    return float(1/(1+np.exp(-z)))

def GDLogistics(X, y, learning_rate=0.01, W=0, b=0):
    Z = [W*x+b for x in X]
    y_pred = [sigmoid(z) for z in Z]
    error = [true - pred for (true, pred) in zip(y,y_pred)]
    W_grad = (1/len(X)) * sum(err * x for (err,x) in zip(error, X))
    b_grad = (1/len(X)) * sum(error)
    W += learning_rate*W_grad
    b += learning_rate*b_grad
    return [W,b]

X = [1, 2, 3]
y = [0, 1, 1]

print(GDLogistics(X,y))