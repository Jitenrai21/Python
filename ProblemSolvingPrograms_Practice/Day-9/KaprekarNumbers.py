#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    res = []
    for i in range(p, q+1):
        n = len(str(i))
        squared = i ** 2
        s= str(squared)
        left = s[:-n]
        right = s[-n:]
        left_val = int(left) if left else 0
        right_val = int(right)
        if left_val + right_val == i:
            res.append(str(i))
    if not res:
        print('INVALID RANGE')
    else:
        print(" ".join(res))
        
if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
