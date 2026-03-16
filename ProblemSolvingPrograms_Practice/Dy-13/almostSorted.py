#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almostSorted(arr):
    # Write your code here
    n = len(arr)
    sorted_arr = sorted(arr)
    if arr == sorted_arr:
        print('yes')
        return
    diffs = [i for i in range(n) if arr[i] != sorted_arr[i]]
    if len(diffs) == 2:
        l, r = diffs[0], diffs[1]
        arr[r], arr[l] = arr[l], arr[r]
        if arr == sorted_arr:
            print('yes')
            print(f'swap {l+1} {r+1}')
            return
        arr[r], arr[l] = arr[l], arr[r]
    l, r = diffs[0], diffs[-1]
    subsegment = arr[l:r+1]
    if arr[:l] + subsegment[::-1] + arr[r+1:] == sorted_arr:
        print('yes')
        print(f'reverse {l+1} {r+1}')
        return
    print('no')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
