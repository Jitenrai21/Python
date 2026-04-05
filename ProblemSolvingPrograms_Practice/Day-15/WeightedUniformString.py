#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    # Write your code here
    weights =  set()
    current_weight = 0
    prev = ''
    for c in s:
        temp = ord(c) - ord('a') + 1
        if c == prev:
            current_weight += temp
        else:
            current_weight = temp
            prev = c
        weights.add(current_weight)
    results = []
    for q in queries:
        if q in weights:
            results.append('Yes')
        else:
            results.append('No')
    return results
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
