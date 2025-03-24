points = [(1, 1, 0), (2, 2, 1), (1, 3, 1), (3, 1, 0)]
def perceptron(points, learning_rate, epochs=1):
    params = [0,0,0] #w1, w2, b
    for _ in range(epochs):
        for x1,x2,y in points:
            y_pred = 1 if params[0]*x1+params[1]*x2+params[2]>=0 else 0
            error = y - y_pred
            params[0] += learning_rate*error*x1
            params[1] += learning_rate*error*x2
            params[2] += learning_rate*error
    return params

print(perceptron(points, 0.1))