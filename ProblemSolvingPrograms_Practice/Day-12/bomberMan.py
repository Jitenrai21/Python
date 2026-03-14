#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    # Write your code here
    if n <= 1:
        return grid
    if n % 2 == 0:
        return ['O' *  len(grid[0]) for _ in range(len(grid))]
    def helper(curr):
        r, c = len(grid), len(grid[0])
        res = [['O' for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if curr[i][j] == 'O':
                    res[i][j] = '.'
                    if i > 0:
                        res[i-1][j] = '.'
                    if i < r-1:
                        res[i+1][j] = '.'
                    if j > 0:
                        res[i][j-1] = '.'
                    if j < c -1:
                        res[i][j+1] = '.'
        return [''.join(row) for row in res]
        
    state_a = helper(grid)
    state_b = helper(state_a)
    
    if n % 4 == 3:
        return state_a
    elif n % 4 == 1:
        return state_b

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
