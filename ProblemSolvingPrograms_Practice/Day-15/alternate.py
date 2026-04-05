#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    # Write your code here
    unique_chars = list(set(s))
    max_length = 0
    for char1, char2 in itertools.combinations(unique_chars, 2):
        temp = [c for c in s if c == char1 or c == char2]
        is_valid = True
        for i in range(len(temp)-1):
            if temp[i] == temp[i+1]:
                is_valid = False
                break
        if is_valid:
            max_length = max(max_length, len(temp))
    return max_length
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
