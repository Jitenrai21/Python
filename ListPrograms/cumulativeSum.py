def cumu(lst):
    result = []
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
        result.append(sum)
    return result
if __name__ == '__main__':
    lst1 = [10,20,30,40,50]
    output = cumu(lst1)
    print(f"Cumulative sum of given list: {output}")
