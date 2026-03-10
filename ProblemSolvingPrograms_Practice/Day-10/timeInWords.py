#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Write your code here
    words = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
        "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
        "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five",
        "twenty six", "twenty seven", "twenty eight", "twenty nine"
    ]
    if m == 0:
        return f"{words[h]} o' clock"
    elif m == 15:
        return f"quarter past {words[h]}"
    elif m == 30:
        return f"half past {words[h]}"
    elif m == 45:
        next_h = h + 1 if h < 12 else 1
        return f"quarter to {words[next_h]}"
    elif m < 30:
        minute_term = 'minute' if m==1 else 'minutes'
        return f"{words[m]} {minute_term} past {words[h]}"
    else:
        past_m = 60 - m
        next_h = h + 1 if h < 12 else 1
        minute_term = 'minute' if m==1 else 'minutes'
        return f"{words[past_m]} {minute_term} to {words[next_h]}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
