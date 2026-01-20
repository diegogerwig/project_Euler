"""
Project Euler Problem 41: Pandigital Prime

We shall say that an n-digit number is pandigital if it makes use of all the digits 
1 to n exactly once.
What is the largest n-digit pandigital prime that exists?

Key Insight:
Sum of digits 1..9 = 45 (Divisible by 3, so never prime)
Sum of digits 1..8 = 36 (Divisible by 3, so never prime)
Sum of digits 1..7 = 28 (Not divisible by 3, candidate for prime!)

Therefore, we start searching from 7-digit numbers downwards.
"""

import itertools
import math

def is_prime(n):
    """Efficiently checks if n is prime."""
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    
    # Check odd divisors up to sqrt(n)
    limit = int(math.isqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

def solve_pandigital_prime():
    # We determined mathematically that n must be 7 or less.
    # We want the LARGEST, so we start with n=7.
    # If we don't find any (unlikely), we would try n=4 (since n=5, n=6 are also div by 3).
    
    # Digits for n=7 in descending order to find the largest first
    digits = "7654321"
    
    # Generate permutations
    # Since the input 'digits' is sorted descending, itertools generates
    # permutations in lexicographical descending order automatically.
    permutations = itertools.permutations(digits)
    
    print(f"Checking permutations of {digits}...")
    
    for p in permutations:
        # Convert tuple ('7', '6', ...) to integer 76...
        num_str = "".join(p)
        num = int(num_str)
        
        # The first prime we hit is guaranteed to be the largest
        if is_prime(num):
            print(f"The largest n-digit pandigital prime is: {num}")
            return

    print("No 7-digit pandigital prime found (unexpected).")

if __name__ == "__main__":
    solve_pandigital_prime()