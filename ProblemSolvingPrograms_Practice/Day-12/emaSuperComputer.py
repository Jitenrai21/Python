#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#

def twoPluses(grid):
    # Write your code here
    R = len(grid)
    C = len(grid[0])
    possible_pluses = []
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'G':
                s = 0
                while True:
                    if (r-s>=0 and r+s<R and c-s>=0 and c+s<C and grid[r-s][c] == 'G' and grid[r+s][c] == 'G' and grid[r][c-s] == 'G' and grid[r][c+s] == 'G'):
                        co_ords = set()
                        for i in range(s+1):
                            co_ords.add((r+i, c))
                            co_ords.add((r-i, c))
                            co_ords.add((r, c+i))
                            co_ords.add((r, c-i))
                        
                        possible_pluses.append({'area':4*s+1, 'co_ords':co_ords})
                        s += 1
                    else:
                        break
    pluses = len(possible_pluses)
    max_prod = 0
    for i in range(pluses):
        for j in range(i+1, pluses):
            p1 = possible_pluses[i]
            p2 = possible_pluses[j]
            if p1['co_ords'].isdisjoint(p2['co_ords']):
                product = p1['area'] * p2['area']
                if max_prod < product:
                    max_prod = product
    return max_prod
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
