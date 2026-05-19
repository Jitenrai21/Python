#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    num = 0
    for i in range(len(s)):
        if i % 3 == 0 and s[i] != 'S':
            num += 1
        elif i % 3 == 1 and s[i] != 'O':
            num += 1
        elif i % 3 == 2 and s[i] != 'S':
            num += 1
    return num
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
