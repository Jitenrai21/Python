#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    # Write your code here
    H = len(A)
    W = len(A[0])
    total_area = 0
    for i in range(H):
        for j in range(W):
            height = A[i][j]
            if height > 0:
                total_area += 2
                up_height = A[i-1][j] if i > 0 else 0
                total_area += max(0, height- up_height)
                
                down_height = A[i+1][j] if i < H - 1 else 0
                total_area += max(0, height - down_height)
                
                left_height = A[i][j-1] if j > 0 else 0
                total_area += max(0, height - left_height)
                
                right_height = A[i][j+1] if j < W - 1 else 0
                total_area += max(0, height - right_height)
    return total_area
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
