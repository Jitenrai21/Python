#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    min_score = scores[0]
    max_score = scores[0]
    
    min_break = 0
    max_break = 0
    
    for i in range(1, len(scores)):
        current_score = scores[i]
        if current_score > max_score:
            max_score = current_score
            max_break += 1
        elif current_score < min_score:
            min_score = current_score
            min_break += 1
    return [max_break, min_break]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
