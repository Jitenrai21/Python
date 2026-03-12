#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    # Write your code here
    counts = Counter(b)
    for val, count in counts.items():
        if val != '_' and count == 1:
            return "NO"
    if counts['_'] > 0:
        return 'YES'
    n = len(b)
    for i in range(n):
        left = b[i-1] if i > 0 else None
        right = b[i+1] if i < n-1 else None
        if b[i] != left and b[i] != right:
            return 'NO'
    return 'YES'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
