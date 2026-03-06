#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    # Write your code here
    n = len(topic)
    team_count = 0
    max_topic = 0
    topics = [int(t, 2) for t in topic]
    for i in range(n):
        for j in range(i+1, n):
            res = topics[i] | topics[j]
            counts = bin(res).count('1')
            if counts > max_topic:
                max_topic = counts
                team_count = 1
            elif counts == max_topic:
                team_count += 1
    return [max_topic, team_count]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
