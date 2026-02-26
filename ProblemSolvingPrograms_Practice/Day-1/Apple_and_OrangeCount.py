#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    ranged_apples = []
    for value in apples:
        ranged = a + value
        ranged_apples.append(ranged)
    ranged_oranges = []
    for value in oranges:
        ranged = b + value
        ranged_oranges.append(ranged)
    fall_count_apples = 0
    fall_count_oranges = 0
    for value in ranged_apples:
        if s <= value <= t:
            fall_count_apples += 1
    for value in ranged_oranges:
        if s <= value <= t:
            fall_count_oranges+=1
    print(fall_count_apples)
    print(fall_count_oranges)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)