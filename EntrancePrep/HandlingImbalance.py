def Balancing(data):
    count_0 = data.count(0)
    count_1 = data.count(1)
    majority = 0 if count_0>count_1 else 1
    minority = 1 - majority
    target = max(count_0, count_1)
    extra = target - min(count_0, count_1)
    return data + [minority]*extra
print(Balancing([0,0,0,1,0]))