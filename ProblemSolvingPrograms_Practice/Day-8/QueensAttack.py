#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    u = n - r_q
    d = r_q - 1
    l = c_q - 1
    r = n- c_q
    
    ur = min(u, r)
    ul = min(u, l)
    dr = min(d, r) 
    dl = min(d, l)
    
    for r_o, c_o in obstacles:
        if c_o == c_q:
            if r_o > r_q:
                u = min(u, r_o - r_q -1)
            else:
                d = min(d, r_q - r_o -1)
        elif r_o == r_q:
            if c_o > c_q:
                r = min(r, c_o - c_q -1)
            else:
                l = min(l, c_q - c_o -1)
        elif abs(r_o - r_q) == abs(c_o - c_q):
            if r_o < r_q and c_o > c_q:
                dr = min(dr, r_q - r_o -1)
            elif r_o < r_q and c_o < c_q:
                dl = min(dl, r_q - r_o -1)
            elif r_o > r_q and c_o > c_q:
                ur = min(ur, r_o - r_q -1)
            elif r_o > r_q and c_o < c_q:
                ul = min(ul, r_o - r_q -1)
    total = u + d + l + r + ur + ul + dr + dl
    return total
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
