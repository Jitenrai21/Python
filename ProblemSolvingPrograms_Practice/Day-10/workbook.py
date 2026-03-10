#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    # Write your code here
    special_count = 0
    page_number = 1
    
    for probs in arr:
        questions = 0
        lower_check = 1
        while probs > 0:
            if probs >= k:
                questions += k
                if lower_check <= page_number <= questions:
                    special_count += 1
                page_number += 1
                lower_check += k
                probs -= k
                
            elif probs < k:
                questions += probs
                if lower_check <= page_number <= questions:
                    special_count += 1
                page_number += 1
                lower_check += probs
                probs = 0
    return special_count      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
