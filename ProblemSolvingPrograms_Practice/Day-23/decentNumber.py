#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#

def decentNumber(n):
    # Write your code here
    fives = n
    threes = 0
    
    while fives >= 0:
        if fives % 3 == 0:
            print('5'*fives+'3'*threes)
            return
        fives -= 5
        threes += 5
    
    print('-1')

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
