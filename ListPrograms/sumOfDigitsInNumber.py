def result(lst):
    res = []
    for ele in lst:
        sum = 0
        for digit in str(ele):
            sum += int(digit)
        res.append(sum)
    return res
if __name__ == '__main__':
    lst = [128,34,56,78,90]
    output = result(lst)
    print(f'The result = {output}')
