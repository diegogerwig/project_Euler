#!/bin/python3

'''
Project Euler #1: Multiples of 3 and 5
If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.
Find the sum of all the multiples of $3$ or $5$ below $1000$.
'''

import math
import os
import random
import re
import sys

def sum_of_multiples(n):
    # Calculate the last multiple of 3 below n
    last_multiple_of_3 = 3 * ((n - 1) // 3)
    # Calculate the last multiple of 5 below n
    last_multiple_of_5 = 5 * ((n - 1) // 5)
    # Calculate the last multiple of 15 below n (to avoid double counting)
    last_multiple_of_15 = 15 * ((n - 1) // 15)
    
    # Calculate the sum of all multiples of 3 below n
    sum_of_3 = (last_multiple_of_3 * (last_multiple_of_3 + 3)) // 6
    # Calculate the sum of all multiples of 5 below n
    sum_of_5 = (last_multiple_of_5 * (last_multiple_of_5 + 5)) // 10
    # Calculate the sum of all multiples of 15 below n
    sum_of_15 = (last_multiple_of_15 * (last_multiple_of_15 + 15)) // 30
    
    # Calculate the total sum
    total_sum = sum_of_3 + sum_of_5 - sum_of_15
    
    return total_sum

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        print(sum_of_multiples(n))
