#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    # Write your code here
    counts =  Counter(s)
    odds = 0
    for value in counts.values():
        if value%2 != 0:
            odds += 1
    if odds <= 1:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
