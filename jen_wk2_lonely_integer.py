#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):

    copy = a
    same = []

    for index, number in enumerate(a):

        for index2, number2 in enumerate(copy):

            if index != index2:

                if number == number2:
                    same.append(number)

    unique_num = list(set(a) - set(same))

    return unique_num[0]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # n = int(input().strip())
    #
    # a = list(map(int, input().rstrip().split()))
    #
    # result = lonelyinteger(a)
    #
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()

    a = [1, 2, 3, 4, 3, 2, 1]

    result = lonelyinteger(a)

    print(result)
