#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    # distances = []
    # for i in range(n):
    #     temp = []
    #     for val in c:
    #         res = abs(val - i)
    #         temp.append(res)
    #     distances.append(min(temp))
    # return max(distances)
    c.sort()
    max_dist = c[0]
    max_dist = max(max_dist, (n-1)-c[-1])
    for i in range(len(c)-1):
        gap = c[i+1] - c[i]
        mid_point = gap//2
        if mid_point > max_dist:
            max_dist = mid_point
    return max_dist
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
