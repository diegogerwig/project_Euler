"""
Project Euler Problem 23: Non-Abundant Sums

A perfect number is a number for which the sum of its proper divisors 
is exactly equal to the number.
A number n is called deficient if the sum of its proper divisors is less 
than n and it is called abundant if this sum exceeds n.

All integers greater than 28123 can be written as the sum of two abundant numbers.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import math

def get_sum_of_divisors(n):
    """
    Calculates the sum of proper divisors of n.
    Standard optimization: iterate only up to sqrt(n).
    """
    if n == 1:
        return 0
    
    total = 1
    limit = int(math.sqrt(n))
    
    for i in range(2, limit + 1):
        if n % i == 0:
            total += i
            # If factors are distinct (e.g., 3 * 4 = 12), add both.
            # If perfect square (e.g., 5 * 5 = 25), add only one 5.
            if i != n // i:
                total += n // i
    return total

def solve_non_abundant_sums():
    # The problem states all integers > 28123 can be written as sum of two abundant numbers.
    limit = 28123
    
    # 1. Find all abundant numbers up to the limit
    abundant_numbers = []
    
    for i in range(12, limit + 1):
        if get_sum_of_divisors(i) > i:
            abundant_numbers.append(i)
            
    # 2. Generate all sums of two abundant numbers
    # We use a set to store the sums because sets are fast for lookups 
    # and handle duplicates automatically.
    abundant_sums = set()
    
    # Nested loop to add every abundant number with every other abundant number
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            
            sum_val = abundant_numbers[i] + abundant_numbers[j]
            
            # Optimization: The list is sorted. If the sum exceeds the limit, 
            # we can stop the inner loop because subsequent sums will be even larger.
            if sum_val > limit:
                break
            
            abundant_sums.add(sum_val)
            
    # 3. Calculate the sum of numbers that CANNOT be written
    # We sum all numbers from 1 to limit, excluding those we found in step 2.
    total_non_abundant_sum = 0
    
    for n in range(1, limit + 1):
        if n not in abundant_sums:
            total_non_abundant_sum += n
            
    print(f"The limit given is: {limit}")
    print(f"Found {len(abundant_numbers)} abundant numbers.")
    print(f"Sum of all non-abundant sums: {total_non_abundant_sum}")

if __name__ == "__main__":
    solve_non_abundant_sums()