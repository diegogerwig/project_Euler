#!/usr/bin/python3

'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
There exists exactly one Pythagorean triplet for which a + b + c = 1000
Find the product abc
'''

import time

start_time = time.time()

def find_pythagorean_triplet(target_sum):
    for a in range(1, target_sum):
        for b in range(a + 1, target_sum):
            c = target_sum - a - b
            if a**2 + b**2 == c**2:
                return a, b, c

def find_triplet_product(target_sum):
    triplet = find_pythagorean_triplet(target_sum)
    if triplet:
        a, b, c = triplet
        product = a * b * c
        return product
    else:
        return None

target_sum = 1000
result = find_triplet_product(target_sum)

if result:
    print(f"The Pythagorean triplet for which a + b + c = {target_sum} is {result}.")
else:
    print(f"No Pythagorean triplet found for the sum {target_sum}.")

end_time = time.time()
execution_time = end_time - start_time
print(f"\033[93mExecution time: {round(execution_time, 6)} seconds\033[0m")