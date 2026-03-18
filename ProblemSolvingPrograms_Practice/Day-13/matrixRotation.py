#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#

def matrixRotation(matrix, r):
    # Write your code here
    m = len(matrix)
    n = len(matrix[0])
    layers = min(m, n) // 2
    for layer in range(layers):
        res = []
        for i in range(layer, n - layer):
            res.append(matrix[layer][i])
        for i in range(layer+1, m -layer):
            res.append(matrix[i][n-1-layer])
        for i in range(n-2-layer, layer-1, -1):
            res.append(matrix[m-1-layer][i])
        for i in range(m-2-layer, layer, -1):
            res.append(matrix[i][layer])
        L = len(res)
        total_rots = r % L
        rot_arr = res[total_rots:] + res[:total_rots]
        idx = 0
        for i in range(layer, n-layer):
            matrix[layer][i] = rot_arr[idx]
            idx += 1
        for i in range(layer+1, m-layer):
            matrix[i][n-1-layer] = rot_arr[idx]
            idx += 1
        for i in range(n-2-layer, layer-1, -1):
            matrix[m-1-layer][i] = rot_arr[idx]
            idx += 1
        for i in range(m-2-layer, layer, -1):
            matrix[i][layer] = rot_arr[idx]
            idx += 1
    for row in matrix:
        print(*(row))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
