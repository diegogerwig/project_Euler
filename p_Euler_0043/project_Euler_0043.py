"""
Project Euler Problem 43: Sub-string Divisibility

Find the sum of all 0 to 9 pandigital numbers with specific sub-string divisibility properties.
Properties:
d2d3d4 % 2 == 0
d3d4d5 % 3 == 0
d4d5d6 % 5 == 0
d5d6d7 % 7 == 0
d6d7d8 % 11 == 0
d7d8d9 % 13 == 0
d8d9d10 % 17 == 0
"""

import itertools

def solve_sub_string_divisibility():
    digits = "0123456789"
    total_sum = 0
    
    # Generate all permutations of 0-9
    # There are 10! = 3,628,800 permutations.
    # Python can handle this iteration in a few seconds.
    permutations = itertools.permutations(digits)
    
    print("Checking permutations...")
    
    for p in permutations:
        # A 10-digit number cannot start with 0
        if p[0] == '0':
            continue
            
        # Optimization: Check constraints from hardest (17) to easiest (2).
        # We access tuple indices: d1 is p[0], d2 is p[1], etc.
        
        # d8d9d10 divisible by 17 (indices 7, 8, 9)
        if int(p[7] + p[8] + p[9]) % 17 != 0:
            continue
            
        # d7d8d9 divisible by 13 (indices 6, 7, 8)
        if int(p[6] + p[7] + p[8]) % 13 != 0:
            continue
            
        # d6d7d8 divisible by 11 (indices 5, 6, 7)
        if int(p[5] + p[6] + p[7]) % 11 != 0:
            continue
            
        # d5d6d7 divisible by 7 (indices 4, 5, 6)
        if int(p[4] + p[5] + p[6]) % 7 != 0:
            continue
            
        # d4d5d6 divisible by 5 (indices 3, 4, 5)
        # Optimization: Last digit (p[5]) must be '0' or '5'
        if p[5] not in ('0', '5'):
            continue
            
        # d3d4d5 divisible by 3 (indices 2, 3, 4)
        if int(p[2] + p[3] + p[4]) % 3 != 0:
            continue
            
        # d2d3d4 divisible by 2 (indices 1, 2, 3)
        # Optimization: Last digit (p[3]) must be even
        if int(p[3]) % 2 != 0:
            continue

        # If we passed all checks, reconstruct the number and add to sum
        num_str = "".join(p)
        total_sum += int(num_str)
        print(f"Found pandigital number: {num_str}")

    print("-" * 30)
    print(f"Sum of all numbers: {total_sum}")

if __name__ == "__main__":
    solve_sub_string_divisibility()