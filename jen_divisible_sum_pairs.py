#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar

def divisibleSumPairs(n, k, ar):
    original = ar
    new_list = []
    counter = 0

    for i in range(0, n):

        for j in range(0, n):

            if i >= j:
                continue

            else:

                if (ar[i] + ar[j]) % k == 0:
                    new_list += ar[i], ar[j]

    return round(len(new_list) / 2)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])
    #
    # k = int(first_multiple_input[1])
    #
    # ar = list(map(int, input().rstrip().split()))

    n = 6
    k = 3
    ar = [1, 3, 2, 6, 1, 2]

    result = divisibleSumPairs(n, k, ar)

    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()