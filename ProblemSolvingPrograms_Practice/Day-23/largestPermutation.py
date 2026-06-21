#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def largestPermutation(k, arr):
    # Write your code here
    pos =  {val:index for index, val in enumerate(arr)}
    for i in range(len(arr)):
        if k == 0:
            break
        ideal = len(arr)-i
        if arr[i] == ideal:
            continue
        current_ideal_idx = pos[ideal]
        current = arr[i]
        arr[i], arr[current_ideal_idx] = arr[current_ideal_idx], arr[i]
        pos[ideal] = i
        pos[current] = current_ideal_idx
        k -= 1
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
