def counter(str):
    count = 0
    while str[count:]:
        count += 1
    return count
result = counter('Inezwa')
print(result)