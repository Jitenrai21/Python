# def outlier(data):
#     mean = sum(data)/len(data)
#     variance = sum((x-mean)**2 for x in data) / len(data)
#     std = variance ** 0.5
#     threshold = 2 * std
#     return [i for i, x in enumerate(data) if abs(x-mean)>threshold]
# print(outlier())

def anamolyDetection(arr):
    mean = sum(arr)/len(arr)
    variance = sum((x-mean)**2 for x in arr)/len(arr)
    std = variance ** 0.5
    threshold = std * 2
    res = []
    for x in arr:
        if abs(x-mean) > threshold:
            res.append(x)
    return res

print(anamolyDetection([1, 2, 1, 50, 3, 4]))