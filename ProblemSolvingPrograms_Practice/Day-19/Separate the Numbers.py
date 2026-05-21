#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    if len(s) < 2 or s[0] == '0':
        print('NO')
        return
        
    n = len(s)
    for i in range(1, n//2+1):
        first_str = s[:i]
        first_num = int(first_str)
        
        test = first_str
        current_num = first_num
        
        while len(test) < n:
            current_num += 1
            test += str(current_num)
        
        if test == s:
            print(f'YES {first_num}')
            return
    print('NO')
        
if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
