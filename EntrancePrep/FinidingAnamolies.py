def outlier(data):
    mean = sum(data)/len(data)
    variance = sum((x-mean)**2 for x in data) / len(data)
    std = variance ** 0.5
    threshold = 2 * std
    return [i for i, x in enumerate(data) if abs(x-mean)>threshold]
print(outlier([1, 2, 1, 50, 3, 2]))