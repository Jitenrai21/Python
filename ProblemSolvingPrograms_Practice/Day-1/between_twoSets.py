#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce
#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def get_gcd(a , b):
    return math.gcd(a, b)

def get_lcm(a, b):
    return abs(a*b) // math.gcd(a, b) 

def getTotalX(a, b):
    # Write your code here
    lcm_a = reduce(get_lcm, a)
    gcd_b = reduce(get_gcd, b)
    multiple = lcm_a
    count = 0
    while multiple <= gcd_b:
        if gcd_b % multiple == 0:
            count += 1
        multiple += lcm_a
    return count
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
