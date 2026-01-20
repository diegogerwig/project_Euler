"""
Project Euler Problem 46: Goldbach's Other Conjecture

It was proposed by Christian Goldbach that every odd composite number can be 
written as the sum of a prime and twice a square.
9 = 7 + 2*1^2
15 = 7 + 2*2^2
...

Find the smallest odd composite that cannot be written as the sum of a prime and twice a square.
"""

import math

def is_prime(n):
    """Efficiently checks if n is prime."""
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def solve_goldbach_other():
    # Start checking odd numbers from 9 (first odd composite)
    n = 9
    
    while True:
        # Step 1: Check if it's composite (not prime)
        if not is_prime(n):
            
            found_proof = False
            
            # Step 2: Try to decompose n = prime + 2*k^2
            # We iterate k starting from 1.
            # We stop when 2*k^2 is larger than n.
            k = 1
            while 2 * k * k < n:
                remainder = n - (2 * k * k)
                
                if is_prime(remainder):
                    found_proof = True
                    break
                
                k += 1
            
            # Step 3: If we went through all k's and found no prime remainder
            if not found_proof:
                print(f"Counter-example found: {n}")
                break
                
        # Move to next odd number
        n += 2

if __name__ == "__main__":
    solve_goldbach_other()