#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    res = []
    srted = sorted(arr)
    minimum = float('inf')
    for i in range(len(arr)-1):
        diff = srted[i+1] - srted[i]
        if diff < minimum:
            minimum = diff
            res = [srted[i], srted[i+1]]
        elif diff == minimum:
            res.extend([srted[i], srted[i+1]])
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
