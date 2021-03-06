#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    swap_rec = {}
    sorted_q = [q[0]] * len(q)
    for j in range(1,len(q)):
        temp = q[j]
        i = j - 1
        while(i >= 0 and sorted_q[i]>temp):
            if sorted_q[i] in swap_rec.keys():
                swap_rec[sorted_q[i]] += 1
                if swap_rec[sorted_q[i]]>2:
                    print( "Too chaotic")
                    return
            else:
                swap_rec[sorted_q[i]] = 1
            sorted_q[i + 1] = sorted_q[i]
            i -= 1
        sorted_q[i+1] = temp
    res = 0
    for key in swap_rec.keys():
        res +=  swap_rec[key]
    print(res)
    return

if __name__ == '__main__':

    q = [1, 2, 5, 3, 4, 7, 8, 6]
    q = [2, 5, 1, 3, 4]
    q = [1, 2, 5, 3, 7, 8, 6, 4]
    print(minimumBribes(q))