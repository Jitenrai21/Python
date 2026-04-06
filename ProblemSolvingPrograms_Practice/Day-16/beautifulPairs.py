#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'beautifulPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY A
#  2. INTEGER_ARRAY B
#

def beautifulPairs(A, B):
    # Write your code here
    count_A = Counter(A)
    count_B = Counter(B)
    beautiful_count = 0
    for val in count_A:
        if val in count_B:
            beautiful_count += min(count_A[val], count_B[val])
    if beautiful_count < len(A):
        return beautiful_count + 1
    else:
        return beautiful_count - 1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
