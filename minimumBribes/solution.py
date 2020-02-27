#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    sorted_q = [q[0]] * len(q)
    for j in range(1,len(q)):
        temp = q[j]
        i = j - 1
        old_temp = q[j]
        while(i >= 0 and sorted_q[i]>temp):
            sorted_q[i + 1] = sorted_q[i]
            i -= 1
        sorted_q[i+1] = temp

    return sorted_q

if __name__ == '__main__':

    q = [1, 2, 5, 3, 4, 7, 8, 6]
    q = [2, 5, 1, 3, 4]
    print(minimumBribes(q))